#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   ChiaCheng Huang(suzuke)
#   E-mail  :   suzuke@hotmail.com
#   Date    :   16/10/10 23:53:27
#   Desc    :   
#

class BaseTemplateAction(object):
    def build(self):
        raise NotImplementedError

class PostbackTemplateAction(BaseTemplateAction):
    def __init__(self, label, data, text=""):
        self.label = label
        self.data = data
        self.text = text

    def build(self):
        return {
            'type' : 'postback',
            'label' : self.label,
            'data' : self.data,
            'text' : self.text
            }

class MsgTemplateAction(BaseTemplateAction):
    def __init__(self, label, text):
        self.label = label
        self.text = text

    def build(self):
        return {
            'type' : 'message',
            'label' : self.label,
            'text' : self.text
            }

def UriTemplateAction(BaseTemplateAction):
    def __init__(self, label, uri):
        self.label = label
        self.uri = uri

    def build(self):
        return {
            'type' : 'uri',
            'label' : self.label,
            'uri' : self.uri
            }
