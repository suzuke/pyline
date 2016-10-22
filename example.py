#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   ChiaCheng Huang(suzuke)
#   E-mail  :   suzuke@hotmail.com
#   Date    :   16/10/13 22:52:53
#   Desc    :   line echo bot
#


from flask import Flask, request
from pyline.events import *
from pyline.client import *
from pyline.messages import *

channelToken = ''
channelSecret = ''

lineClient = LineClient(channelToken)
app = Flask(__name__)

@app.route('/callback', methods=['POST'])
def handleCallback():
    eventRequestHandler = EventRequestHandler(request, channelSecret)
    events = eventRequestHandler.getEvents()
    for event in events:
        message = event.getMessage()
        messageType = message.getType()
        if messageType == 'text':
            '''reply message'''
            msg = TextMsg(message.getText())
            lineClient.replyMessage(event.getReplyToken(), msg)
        elif messageType == "sticker":
            '''another method to reply message'''
            msg = StickerMsg(message.getPackageId(), message.getStickerId())
            lineClient.pushMessage(event.getId(), msg)

    return ''

if __name__ == "__main__":
    app.run()
