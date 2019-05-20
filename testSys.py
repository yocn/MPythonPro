#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, time
from operator import attrgetter


def test():
    return


class File:
    def __init__(self, timeStamp, timeString, path, name):
        self.timeStamp = timeStamp
        self.timeString = timeString
        self.path = path
        self.name = name

    def __str__(self):
        return "File(" + self.timeString + " " + self.name + " " + str(self.timeStamp) + ")\n"

    def __repr__(self):
        return "File(" + self.timeString + " " + self.name + " " + str(self.timeStamp) + ")\n"


def get_files(ppath):
    file_names = os.listdir(ppath)
    files = []
    for name in file_names:
        if not name.startswith("."):
            file_path = unicode(name, 'utf8')
            read_path = ppath + "/" + file_path
            time_stamp = os.path.getctime(read_path)
            show_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time_stamp))

            m_file = File(time_stamp, show_time, read_path, file_path)
            files.append(m_file)
    files.sort(key=attrgetter('timeStamp'))
    return files


pwd = os.getcwd()
cgi_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + "./MPythonPro/")
current_files = get_files(cgi_path)

print "Content-type:text/html"
print  # 空行，告诉服务器结束头部
print '<html>'
print '<head>'
print '<meta charset="utf-8">'
print '<title>Hello World - 我的第一个 CGI 程序！</title>'
print '</head>'
print '<body>'
print '<h2>下载列表</h2>'
for simple_file in current_files:
    print '<a href="%s" download="%s">%s %s</a><br>' % (
        simple_file.path, simple_file.name, simple_file.timeString, simple_file.name)
print '</body>'
print '</html>'
