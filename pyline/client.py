#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   ChiaCheng Huang(suzuke)
#   E-mail  :   suzuke@hotmail.com
#   Date    :   16/10/12 23:49:46
#   Desc    :   
#

import requests
import json
import base64
import hashlib
import hmac

try:
        from urlparse import urlparse, urljoin
except:
        from urllib.parse import urlparse, urljoin

from events import EventHandler

class LineClient(object):
    def __init__(self, channelToken, channelSecret=""):
        self.channelToken = channelToken
        self.channelSecret = channelSecret
        self.baseApiUrl = "https://api.line.me/v2/bot"
        self.headers = {
                'Content-Type' : 'application/json',
                'Authorization' : 'Bearer {}'.format(self.channelToken),
                }

    def parseEventRequest(self, request):
        signature = request.headers.get("X-Line-Signature")
        payload = request.get_data()
        if self.__validateSignature(signature, payload):
            events = EventHandler(payload).getEvents()
            return events
        else:
            raise AssertionError("Signature validate failed, ignores all events.")

    def replyMessage(self, replyToken, message):
        data = json.dumps({
            'replyToken' : replyToken,
            'messages' : message.build()
            })
        return requests.post(self.__createUrl("message", "reply"), headers=self.headers, data=data)

    def pushMessage(self, to, message):
        data = json.dumps({
            'to' : to,
            'messages' : message.build()
            })
        return requests.post(self.__createUrl("message", "push"), headers=self.headers, data=data)

    def getContent(self, messageId):
        return requests.get(self.__createUrl("message", str(messageId), "content"), headers=self.headers)

    def getProfile(self, userId):
        return requests.get(self.__createUrl("profile", str(userId)), headers=self.headers)

    def leaveGroup(self, groupId):
        return requests.post(self.__createUrl("group", str(groupId), "leave"), headers=self.headers)

    def leaveRoom(self, roomId):
        return requests.post(self.__createUrl("room", str(roomId), "leave"), headers=self.headers)

    def __validateSignature(self, signature, payload):
        if self.channelSecret == "":
            return True

        return self.__compare_digest(
                signature.encode('utf-8'),
                base64.b64encode(
                    hmac.new(
                        self.channelSecret.encode('utf-8'),
                        msg=payload,
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

    def __createUrl(self, *paths):
        parsed_url = urlparse(self.baseApiUrl)
        path = parsed_url.path.split('/')
        path.extend(paths)
        path = '/'.join(path)
        return urljoin(parsed_url.geturl(), path)
