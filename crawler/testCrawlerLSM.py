#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2, urllib, bs4, os, time, logging, random


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


# locol = "/Users/yocn/python/res/MM131/"
# locol = "/Users/y/PythonWorkSpace/MM131/"
locol = "/Users/y/PythonWorkSpace/LSM/"


def test():
    # 20000-20700
    start_index = 20000
    end_index = 20100
    for i in range(start_index, end_index):
        download_mmm131(i)
    return


sample = "https://i.gzjxfw.com:116/k/1178/T/XiuRen/1319/1319_001_bz2_1200_1800.jpg"


def download_mmm131(index):
    total_index = 0
    for i in range(1, 6):
        url = "https://www.lsm.me/thread-%d-%d-1.html" % (index, i)
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

        # html = urllib2.urlopen(url).read()

        # print html
        soup = bs4.BeautifulSoup(html, "html.parser", from_encoding="utf-8")
        # print soup.prettify()
        all_img = soup.find_all("img")
        pic_list = []
        current_dir = locol + "" + str(index) + "/"
        for img in all_img:
            total_index += 1
            src = img.attrs["src"]
            # print len(src), len(sample)
            if len(src) >= len(sample):
                name = str(total_index)
                locol_path = locol + "" + str(index) + "/" + name + ".jpg"
                pic = Pic(src, name, locol_path)
                print pic.url + " " + pic.path + " " + pic.desc
                pic_list.append(pic)

            # parent = img.parent;
            # pparent = parent.parent;
            # attrs = pparent.attrs
            # # print img, parent, pparent
            #
            # if not attrs is None and attrs.has_key("class") and attrs["class"][0].encode('utf-8') == 'adw':
            #     print pparent, len(pparent.contents)
            #     print pparent, len(pparent.contents)
            #     for i in range(len(pparent.contents)):
            #         total_index += 1
            #         name = str(total_index)
            #         curr = parent.contents[i]
            #         print curr
            #         locol_path = locol + "" + str(index) + "/" + name + ".jpg"
            #         pic = Pic(curr.attrs["src"], name, locol_path)
            #         print pic.url + " " + pic.path + " " + pic.desc
            #         pic_list.append(pic)

        for pic in pic_list:
            if not os.path.exists(current_dir):
                os.mkdir(current_dir)
            print "-------------开始下载---------------", pic.url, pic.path
            urllib.urlretrieve(pic.url, pic.path)

        time.sleep(3)
    return
