#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   ChiaCheng Huang(suzuke)
#   E-mail  :   suzuke@hotmail.com
#   Date    :   16/10/10 22:43:19
#   Desc    :   
#

class BaseSize(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def build(self)
        return {
            'height' : self.height,
            'width' : self.width
            }


