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
try:
        from urlparse import urlparse, urljoin
except:
        from urllib.parse import urlparse, urljoin


class LineClient(object):
    def __init__(self, channelToken):
        self.channelToken = channelToken
        self.baseApiUrl = "https://api.line.me/v2/bot"
        self.headers = {
                'Content-Type' : 'application/json',
                'Authorization' : 'Bearer {}'.format(self.channelToken),
                }

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
        print self.headers
        #print self.__createUrl("message", str(messageId), "content")
        return requests.get(self.__createUrl("message", str(messageId), "content"), headers=self.headers)

    def getProfile(self, userId):
        return requests.get(self.__createUrl("profile", str(userId)), headers=self.headers)

    def leaveGroup(self, groupId):
        return requests.post(self.__createUrl("group", str(groupId), "leave"), headers=self.headers)

    def leaveRoom(self, roomId):
        return requests.post(self.__createUrl("room", str(roomId), "leave"), headers=self.headers)

    def __createUrl(self, *paths):
        parsed_url = urlparse(self.baseApiUrl)
        path = parsed_url.path.split('/')
        path.extend(paths)
        path = '/'.join(path)
        return urljoin(parsed_url.geturl(), path)
