#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   ChiaCheng Huang(suzuke)
#   E-mail  :   suzuke@hotmail.com
#   Date    :   16/10/10 23:15:29
#   Desc    :   
#

class BaseTemplateMsg(object):
    def build(self):
        raise NotImplementedError

class ButtonsTemplateMsg(BaseTemplateMsg):
    def __init__(self, thumbnailImageUrl, title, text, actions):
        self.thumbnailImageUrl = thumbnailImageUrl
        self.title = title
        self.text = text
        self.actions = actions

    def build(self):
        return {
            'type' : 'buttons',
            'thumbnailImageUrl' : self.thumbnailImageUrl,
            'title' : self.title,
            'text' : self.text,
            'actions' : [
                action.build() for action in self.actions
                ]
            }

class ConfirmTemplateMsg(BaseTemplateMsg):
    def __init__(self, text, actions):
        self.text = text
        self.actions = actions

    def build(self):
        return {
            'type' : 'confirm',
            'text' : self.text,
            'actions' : [
                action.build() for action in self.actions
                ]
            }

def CarouselTemplateMsg(BaseTemplateMsg):
    def __init__(self, columns):
        self.colums = colums

    def build(self):
        return {
            'type' : 'carousel',
            'columns' : [
                column.build() for column in self.columns
                ]
            }
