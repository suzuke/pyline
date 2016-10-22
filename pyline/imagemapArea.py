#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   ChiaCheng Huang(suzuke)
#   E-mail  :   suzuke@hotmail.com
#   Date    :   16/10/10 21:28:42
#   Desc    :   
#

class ImagemapArea(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def build(self):
        return {
            'x' : self.x,
            'y' : self.y,
            'width' : self.width,
            'height' : self.height
            }

