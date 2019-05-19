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


locol = "/Users/y/PythonWorkSpace/mm131/"


def test():
    # 3000-4900
    start_index = 3016
    end_index = 3017
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
        html = urllib2.urlopen(request).read()

        # html = urllib2.urlopen(url).read()

        # print html
        soup = bs4.BeautifulSoup(html, "html.parser", from_encoding="utf-8")
        print soup.prettify()
        all_img = soup.find_all("img")
        pic_list = []
        current_dir = locol + "" + str(index) + "/"
        # 如果img标签里面含有data-original属性则把data-original标签的内容也就是http链接地址存储到img_list中
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
        time.sleep(1)
    return
