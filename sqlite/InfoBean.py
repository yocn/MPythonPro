#!/usr/bin/python
# -*- coding: UTF-8 -*-

class InfoBean:
    '爬虫存储类'

    def __init__(self, id, name, url, status, path, desc):
        self.id = id
        self.name = name
        self.url = url
        self.status = status
        self.path = path
        self.desc = desc

    def __str__(self):
        return "File(" + str(self.id) + " " + self.name + " " + str(self.url) + " " + str(self.status) + " " + str(
            self.path) + " " + str(self.desc) + ")"

    def __repr__(self):
        return "File(" + str(self.id) + " " + self.name + " " + str(self.url) + " " + str(self.status) + " " + str(
            self.path) + " " + str(self.desc) + ")"
