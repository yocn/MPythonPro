#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2, urllib, os, time, json

print str(time.time()).replace(".", "0")


class Pic:
    def __init__(self, url, desc, path):
        self.url = url
        self.desc = desc
        self.path = path


# locol = "/Users/yocn/python/res/DUOWAN/"
# locol = "/Users/y/PythonWorkSpace/MM131/"
locol = "/Users/y/PythonWorkSpace/DUOWAN/"


def test():
    # 20000-20700
    start_index = 137882
    end_index = 138930
    for i in range(start_index, end_index):
        download_pic(i)
    return


def download_pic(index):
    curr_time = str(time.time()).replace(".", "0")
    url = "http://tu.duowan.com/index.php?r=show/getByGallery/&gid=%d&_=%s" % (index, curr_time)
    print "开始执行Task %s" % url
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
    if html.strip() == '':
        return
    dict = json.loads(html, encoding="GBK")
    # print raw.keys()
    # print dict[u'picInfo']
    pic_list = []
    pic_info = dict[u'picInfo']
    current_dir = locol + "" + str(index) + "/"
    for info in pic_info:
        source = info[u'source']
        desc = info[u'add_intro']
        suffix = '.gif'
        if source.endswith("gif"):
            suffix = '.gif'
        elif source.endswith("jpg"):
            suffix = '.jpg'
        else:
            return
        path = current_dir + desc + suffix
        pic = Pic(source, desc, path)
        pic_list.append(pic)

    for pic in pic_list:
        if not os.path.exists(current_dir):
            os.mkdir(current_dir)
        print "-------------开始下载---------------", pic.url, pic.path
        urllib.urlretrieve(pic.url, pic.path)

    print '休息一下，休息3s'
    time.sleep(3)
    return
