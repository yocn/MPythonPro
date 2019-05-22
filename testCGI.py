#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, time
from operator import attrgetter


class File:
    def __init__(self, timeStamp, timeString, path, name, size):
        self.timeStamp = timeStamp
        self.timeString = timeString
        self.path = path
        self.name = name
        self.size = size

    def __str__(self):
        return "File(" + self.timeString + " " + self.name + " " + str(self.timeStamp) + ")\n"

    def __repr__(self):
        return "File(" + self.timeString + " " + self.name + " " + str(self.timeStamp) + ")\n"


def get_file_size(file_path):
    f_size = os.path.getsize(file_path)
    f_size = f_size / float(1024 * 1024)
    return round(f_size, 2)


def get_files(ppath):
    file_names = os.listdir(ppath)
    files = []
    for name in file_names:
        if not name.startswith("."):
            file_path = unicode(name, 'utf8')
            read_path = ppath + "/" + file_path
            time_stamp = os.path.getctime(read_path)
            show_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time_stamp))
            size = get_file_size(read_path)
            m_file = File(time_stamp, show_time, read_path, file_path, size)
            files.append(m_file)
    files.sort(key=attrgetter('timeStamp'))
    return files


pwd = os.getcwd()
# debug_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + "../debug/")
# release_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + "../release/")
debug_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + "")
release_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + "")
debug_files = get_files(debug_path)
release_files = get_files(release_path)
max = 0
if len(debug_files) > len(release_files):
    max = len(debug_files)
else:
    max = len(release_files)
max = 100 + max * 21
print "Content-type:text/html"
print  # 空行，告诉服务器结束头部
print '<html>'
print '<head>'
print '<meta charset="utf-8">'
print '<title>Android Apks</title>'
print '</head>'
print '<body>'
print '<h4>当前访问时间：%s</h4>' % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
print '<div id="container" style="width:1610px">'
print '<div id="content" style="background-color:#EEEEEE;height:%dpx;width:800px;float:left;">' % max
print '<h2>&nbsp;下载Debug列表</h2>'
for simple_file in debug_files:
    print '&nbsp;%s&nbsp;&nbsp;&nbsp;%s MB&nbsp;&nbsp;<a href="/debug/%s" download="%s">%s</a><br>' % (
        simple_file.timeString, simple_file.size, simple_file.name, simple_file.name, simple_file.name)
print '</div>'
print '<div id="content" style="background-color:#FFFFFF;height:400px;width:10px;float:left;">'
print '</div>'
print '<div id="content" style="background-color:#EEEEEE;height:%dpx;width:800px;float:left;">' % max
print '<h2>&nbsp;下载Release列表</h2>'
for simple_file in release_files:
    print '&nbsp;%s&nbsp;&nbsp;&nbsp;%s MB&nbsp;&nbsp;<a href="/release/%s" download="%s">%s</a><br>' % (
        simple_file.timeString, simple_file.size, simple_file.name, simple_file.name, simple_file.name)
print '</div>'
print '</div>'
print '</body>'
print '</html>'
