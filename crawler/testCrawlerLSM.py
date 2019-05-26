#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2, urllib, bs4, os, time


class Pic:
    def __init__(self, url, desc, path):
        self.url = url
        self.desc = desc
        self.path = path


locol = "/Users/y/PythonWorkSpace/LSM/"


def test():
    # 20000-20700
    start_index = 20000
    end_index = 20100
    for i in range(start_index, end_index):
        download_pic(i)
    return


sample = "https://i.gzjxfw.com:116/k/1178/T/XiuRen/1319/1319_001_bz2_1200_1800.jpg"


def download_pic(index):
    total_index = 0
    for i in range(1, 6):
        url = "https://www.lsm.me/thread-%d-%d-1.html" % (index, i)
        print url
        # 添加header模拟浏览器，必要的话尽量填完整，简单的话就只加UA
        request = urllib2.Request(url)  # Request参数有三个，url,data,headers,如果没有data参数，那就得按我这样的写法
        request.add_header("User-Agent",
                           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36")
        request.add_header("Accept-Language", "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,fr;q=0.6")
        request.add_header("Accept",
                           "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3")

        response = urllib2.urlopen(request)
        # 可能某些情况下会失败，如果不想打断爬取可以加上这个，如果想查原因，推荐链接和失败code存数据库，后续可以查原因
        if response.code != 200:
            return
        html = response.read()

        soup = bs4.BeautifulSoup(html, "html.parser", from_encoding="utf-8")
        # print soup.prettify()
        all_img = soup.find_all("img")
        pic_list = []
        # 本地存储路径
        current_dir = locol + "" + str(index) + "/"
        for img in all_img:
            # 用来做文件名字，当然也可以抓取链接其他内容作为文件名
            total_index += 1
            # 获取src属性，也就是图片的真实地址
            src = img.attrs["src"]
            # 这个判断其实是为了筛出来我真正想要的图片地址，因为还有一些网站的logo之类的小图片
            if len(src) >= len(sample):
                name = str(total_index)
                locol_path = locol + "" + str(index) + "/" + name + ".jpg"
                pic = Pic(src, name, locol_path)
                print pic.url + " " + pic.path + " " + pic.desc
                pic_list.append(pic)

            # 这里也是一种方法来筛选图片，我们观察看我们想要的img的parent的parent的class属性都是adw，可以用这个来做判断条件，但是这样效率可能更低些~
            # 而且好像有好像有bug，我最终没有用这个方法
            # parent = img.parent;
            # pparent = parent.parent;
            # attrs = pparent.attrs
            #
            # if not attrs is None and attrs.has_key("class") and attrs["class"][0].encode('utf-8') == 'adw':
            #     for i in range(len(pparent.contents)):
            #         total_index += 1
            #         name = str(total_index)
            #         curr = parent.contents[i]
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
