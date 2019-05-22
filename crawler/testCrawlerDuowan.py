#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2, urllib, os, time, json

print str(time.time()).replace(".", "0")


class Pic:
    def __init__(self, url, desc, path):
        self.url = url
        self.desc = desc
        self.path = path

    # def __str__(self):
    #     return "File(" + self.path + " " + self.desc + " " + self.name + ")\n"
    #
    # def __repr__(self):
    #     return "File(" + self.path + " " + self.desc + " " + self.name + ")\n"


locol = "/Users/yocn/python/res/DUOWAN/"


# locol = "/Users/y/PythonWorkSpace/MM131/"
# locol = "/Users/y/PythonWorkSpace/LSM/"


def test():
    # 20000-20700
    start_index = 138897
    end_index = 138898
    for i in range(start_index, end_index):
        download_pic(i)
    return


def download_pic(index):
    curr_time = str(time.time()).replace(".", "0")
    url = "http://tu.duowan.com/index.php?r=show/getByGallery/&gid=%d&_=%s" % (index, curr_time)
    print url
    request = urllib2.Request(url)  # Request参数有三个，url,data,headers,如果没有data参数，那就得按我这样的写法
    request.add_header("User-Agent",
                       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36")
    request.add_header("Accept-Language", "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,fr;q=0.6")
    request.add_header("Accept",
                       "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3")

    response = urllib2.urlopen(request)
    # print response.code
    if response.code != 200:
        return
    html = response.read()
    raw = json.dumps(html)
    print html
    print "------------------------------------------------------------------------------------------"
    print raw
    dict = json.loads(html, encoding="GBK")
    # print raw.keys()
    print dict[u'picInfo']

    # for pic in pic_list:
    #     if not os.path.exists(current_dir):
    #         os.mkdir(current_dir)
    #     print "-------------开始下载---------------", pic.url, pic.path
    #     urllib.urlretrieve(pic.url, pic.path)

    time.sleep(3)
    return
