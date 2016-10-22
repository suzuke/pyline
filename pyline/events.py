#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   ChiaCheng Huang(suzuke)
#   E-mail  :   suzuke@hotmail.com
#   Date    :   16/10/10 23:57:05
#   Desc    :   
#

import json
import sys
import base64
import hashlib
import hmac

class SourceHandler(object):
    def __init__(self, source):
        self.source = source
        self.sourceDict = {
                'user' : 'UserSource',
                'group' : 'GroupSource',
                'room' : 'RoomSource'
                }

    def getSource(self):
        sourceObj = getattr(sys.modules[__name__], str(self.sourceDict.get(self.source["type"])))
        return sourceObj(self.source)

class BaseSource(object):
    def __init__(self, source):
        self.source = source

    def getType(self):
        return self.source["type"]

    def getId(self):
        raise NotImplementedError

class UserSource(BaseSource):
    def getId(self):
        return self.source["userId"]

class GroupSource(BaseSource):
    def getId(self):
        return self.source["groupId"]

class RoomSource(BaseSource):
    def getId(self):
        return self.source["roomId"]


class EventRequestHandler(object):
    def __init__(self, request, channelSecret=""):
        self.signature = request.headers.get("X-Line-Signature")
        self.data = request.get_data()
        self.events = json.loads(self.data)["events"]
        self.channelSecret = channelSecret
        self.eventDict = {
                'message' : 'MessageEvent',
                'follow' : 'FollowEvent',
                'unfollow' : 'UnfollowEvent',
                'join' : 'JoinEvent',
                'leave' : 'LeaveEvent',
                'postback' : 'PostBackEvent',
                'beacon' : 'BeaconEvent'
                }

    def __validateSignature(self):
        if self.channelSecret == "":
            return True

        return self.__compare_digest(
                self.signature.encode('utf-8'),
                base64.b64encode(
                    hmac.new(
                        self.channelSecret.encode('utf-8'),
                        msg=self.data,
                        digestmod=hashlib.sha256
                        ).digest()
                    )
                )
    def __compare_digest(self, a, b):
        """Time-constant comparison. Less secure than hmac.compare_digest
        See http://legacy.python.org/dev/peps/pep-0466/
        """
        if len(a) != len(b):
            return False
        flag = 0
        for x, y in zip(a, b):
            flag |= ord(x) ^ ord(y)
        return flag == 0

    def getEvents(self):
        events = []
        if self.__validateSignature():
            for event in self.events:
                eventObj =  getattr(sys.modules[__name__], str(self.eventDict.get(event["type"])))
                events.append(eventObj(event))
        else:
            print "Failed to validate signature, ignore all events."
        return events

class BaseEvent(object):
    def __init__(self, event):
        self.event  = event
        self.source = SourceHandler(self.event["source"]).getSource()

    def getType(self):
        return self.event["type"]

    def getTimeStamp(self):
        return self.event["timestamp"]
    
    def getSource(self):
        return self.source

    def getId(self):
        return self.source.getId()

    def getSourceType(self):
        return self.source.getType()

class MessageHandler(object):
    def __init__(self, message):
        self.message = message
        self.messageDict = {
                'text' : 'TextEventMessage',
                'image' : 'ImageEventMessage',
                'video' : 'VideoEventMessage',
                'audio' : 'AudioEventMessage',
                'location' : 'LocationEventMessage',
                'sticker' : 'StickerEventMessage'
                }

    def getMessage(self):
        messageObj = getattr(sys.modules[__name__], str(self.messageDict.get(self.message["type"])))
        return messageObj(self.message)

class MessageEvent(BaseEvent):
    def __init__(self, event):
        super(MessageEvent, self).__init__(event)
        self.message = MessageHandler(self.event["message"]).getMessage()

    def getReplyToken(self):
        return self.event["replyToken"]

    def getMessage(self):
        return MessageHandler(self.event["message"]).getMessage()

class FollowEvent(BaseEvent):
    def getReplyToken(self):
        return self.event["replyToken"]

class UnfollowEvent(BaseEvent):
    pass

class JoinEvent(BaseEvent):
    def getReplyToken(self):
        return self.event["replyToken"]

class LeaveEvent(BaseEvent):
    pass

class PostBackEvent(BaseEvent):
    def __init__(self, event):
        super(PostBackEvent, self).__init__(event)
        self.postback = self.event["postback"]

    def getReplyToken(self):
        return self.event["replyToken"]

    def getData(self):
        return self.postback["data"]

class BeaconEvent(BaseEvent):
    def __init__(self, event):
        super(BeaconEvent, self).__init__(event)
        self.beacon = self.event["beacon"]

    def getReplyToken(self):
        return self.event["replyToken"]

    def getBeacon(self):
        return self.beacon

    def getHwid(self):
        return self.beacon["hwid"]

    def getBeaconType(self):
        return self.beacon["type"]

class BaseEventMessage(object):
    def __init__(self, message):
        self.message = message

    def getId(self):
        return self.message["id"]

    def getType(self):
        return self.message["type"]

class TextEventMessage(BaseEventMessage):
    def getText(self):
        return self.message["text"]

class ImageEventMessage(BaseEventMessage):
    pass

class VideoEventMessage(BaseEventMessage):
    pass

class AudioEventMessage(BaseEventMessage):
    pass

class LocationEventMessage(BaseEventMessage):
    def getTitle(self):
        return self.message["title"]

    def getAddress(self):
        return self.message["address"]

    def getLatitude(self):
        return self.message["latitude"]

    def getLongitude(self):
        return self.message["longitude"]

class StickerEventMessage(BaseEventMessage):
    def getPackageId(self):
        return self.message["packageId"]

    def getStickerId(self):
        return self.message["stickerId"]
