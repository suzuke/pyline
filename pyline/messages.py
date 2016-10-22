#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   ChiaCheng Huang(suzuke)
#   E-mail  :   suzuke@hotmail.com
#   Date    :   16/10/10 17:41:14
#   Desc    :   
#
import random

class BaseMsg(object):
    def build(self):
        raise NotImplementedError

class TextMsg(BaseMsg):
    def __init__(self, *text):
        self.text = text

    def build(self):
        return [{
            'type' : 'text',
            'text' : text
            } for text in self.text]

class RandomTextMsg(TextMsg):
    def build(self):
        return [{
            'type' : 'text',
            'text' : random.choice(self.text)
            }]

class ImageMsg(BaseMsg):
    def __init__(self, originalContentUrl, previewImageUrl):
        self.originalContentUrl = originalContentUrl
        self.previewImageUrl = previewImageUrl

    def build(self):
        return [{
            'type' : 'image',
            'originalContentUrl' : self.originalContentUrl,
            'previewImageUrl' : self.previewImageUrl
            }]

class VideoMsg(BaseMsg):
    def __init__(self, originalContentUrl, previewImageUrl):
        self.originalContentUrl = originalContentUrl
        self.previewImageUrl = previewImageUrl

    def build(self):
        return [{
            'type' : 'video',
            'originalContentUrl' : self.originalContentUrl,
            'previewImageUrl' : self.previewImageUrl
            }]

class AudioMsg(BaseMsg):
    def __init__(self, originalContentUrl, duration):
        self.originalContentUrl = originalContentUrl
        self.duration = duration

    def build(self):
        return [{
            'type' : 'audio',
            'originalContentUrl' : self.originalContentUrl,
            'duation' : self.duation
            }]

class LocationMsg(BaseMsg):
    def __init__(self, title, address, latitude, longitude):
        self.title = title
        self.address = address
        self.latitude = latitude
        self.longitude = longitude

    def build(self):
        return [{
            'type' : 'location',
            'title' : self.title,
            'address' : self.address,
            'latitude' : self.latitude,
            'longitude' : self.longitude
            }]

class StickerMsg(BaseMsg):
    def __init__(self, packageId, stickerId):
        self.packageId = packageId
        self.stickerId = stickerId

    def build(self):
        return [{
            'type' : 'sticker',
            'packageId' : self.packageId,
            'stickerId' : self.stickerId
            }]

class ImagemapMsg(BaseMsg):
    def __init__(self, baseUrl, altText, baseSize, actions):
        self.baseUrl = baseUrl
        self.altText = altText
        self.baseSize = baseSize
        slef.actions = actions

    def build(self):
        return [{
            'type' : 'imagemap',
            'baseUrl' : self.baseUrl,
            'altText' : self.altText,
            'baseSize' : self.baseSize.build(),
            'actions' : [
                action.build() for action in self.actions
                ]
            }]

class TemplateMsg(BaseMsg):
    def __init__(self, altText, msgTemplate):
        self.altText = altText
        self.msgTemplate = msgTemplate

    def build(self):
        return [{
            'type' : 'template',
            'altText' : self.altText,
            'template' : self.msgTemplate.build()
            }]
