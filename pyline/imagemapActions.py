#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   ChiaCheng Huang(suzuke)
#   E-mail  :   suzuke@hotmail.com
#   Date    :   16/10/10 21:34:32
#   Desc    :   
#

from ImagemapArea import *

class ImagemapBaseAction(object):
    def build(self):
        raise NotImplementedError

class ImagemapUriAction(ImagemapBaseAction):
    def __init__(self, linkUri, imagemapArea):
        self.linUri = linkUri
        self.area = imagemapArea

    def build(self):
        return {
            'type' : 'uri',
            'linkUri' : self.linkUri,
            'area' : self.area.build()
            }

def ImagemapMsgAction(ImagemapBaseAction):
    def __init__(self, text, imagemapArea):
        self.text = text
        self.area = imagemapArea

    def build(self):
        return {
            'type' : 'message',
            'text' : self.text,
            'area' : self.area.build()
            }
