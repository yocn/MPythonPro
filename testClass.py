#!/usr/bin/python
# -*- coding: UTF-8 -*-

class File:
    def __init__(self, timeStamp, timeString, path, name):
        self.timeStamp = timeStamp
        self.timeString = timeString
        self.path = path
        self.name = name

    def __str__(self):
        return "File(" + self.timeString + " " + self.name + " " + str(self.timeStamp) + " " + str(self.path) + ")\n"

    def __repr__(self):
        return "File(" + self.timeString + " " + self.name + " " + str(self.timeStamp) + " " + str(self.path) + ")\n"


def test():
    m_file = File("time_stamp", "show_time", "read_path", "file_path")
    print m_file
    return
