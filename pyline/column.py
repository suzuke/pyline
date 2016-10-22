#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   ChiaCheng Huang(suzuke)
#   E-mail  :   suzuke@hotmail.com
#   Date    :   16/10/10 23:41:53
#   Desc    :   
#

class Column(object):
    def __init__(self, thumbnailImageUrl, title, text, templateActions):
        self.thumbnailImageUrl = thumbnailImageUrl
        self.title = title
        self.text = text
        self.templateActions = templateActions

    def build(self):
        return {
            'thumbnailImageUrl' : self.thumbnailImageUrl,
            'title' : self.title,
            'text' : self.text,
            'acions' : [
                action.build() for action in self.templateActions
                ]
            }
