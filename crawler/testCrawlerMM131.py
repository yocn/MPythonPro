#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2, urllib, bs4, os, time, logging


class Pic:
    def __init__(self, path, desc, name):
        self.path = path
        self.desc = desc
        self.name = name

    # def __str__(self):
    #     return "File(" + self.path + " " + self.desc + " " + self.name + ")\n"
    #
    # def __repr__(self):
    #     return "File(" + self.path + " " + self.desc + " " + self.name + ")\n"


locol = "/Users/yocn/python/res/MM131/"
locol = "/Users/y/PythonWorkSpace/"


def test():
    # 3000-4900
    start_index = 3018
    end_index = 3019
    for i in range(start_index, end_index):
        download_mmm131(i)
    return


def download_mmm131(index):
    for i in range(2, 3):
        if i == 1:
            url = "http://www.mm131.com/xinggan/%d.html" % index
        else:
            url = "http://www.mm131.com/xinggan/%d_%d.html" % (index, i)
        print url
        request = urllib2.Request(url)  # Request参数有三个，url,data,headers,如果没有data参数，那就得按我这样的写法
        request.add_header("User-Agent",
                           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36")
        request.add_header("Accept-Language", "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,fr;q=0.6")
        request.add_header("Accept",
                           "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3")

        html = urllib2.urlopen(request).read()

        # html = urllib2.urlopen(url).read()

        # print html
        soup = bs4.BeautifulSoup(html, "html.parser", from_encoding="utf-8")
        print soup.prettify()
        all_img = soup.find_all("img")
        pic_list = []
        current_dir = locol + "" + str(index) + "/"
        img = all_img[0]
        print img
        if "src" in img.attrs:
            locol_path = locol + "" + str(index) + "/" + img.attrs["alt"] + ".jpg"
            pic = Pic(img.attrs["src"], img.attrs["alt"], locol_path)
            print pic.path + " " + pic.name + " " + pic.desc
            pic_list.append(pic)

        for pic in pic_list:
            if not os.path.exists(current_dir):
                os.mkdir(current_dir)
            print "开始下载", pic.path, pic.name
            # print "开始下载", (img)
            urllib.urlretrieve(pic.path, pic.name)
        time.sleep(3)
    return
