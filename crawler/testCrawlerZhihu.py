#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2, urllib, bs4


def test():
    url = "https://www.zhihu.com/question/35005800/answer/61498512"
    response1 = urllib2.urlopen(url)
    html = response1.read()

    soup = bs4.BeautifulSoup(html, "html.parser", from_encoding="utf-8")
    print soup.prettify()
    all_img = soup.find_all("img")
    img_list = []
    for img in all_img:
        # 如果img标签里面含有data-original属性则把data-original标签的内容也就是http链接地址存储到img_list中
        if "data-original" in img.attrs:
            img_list.append(img.attrs["data-original"])

    for img in img_list:
        print "开始下载", (img)
        # https://pic4.zhimg.com/49ce58f2c038c709968a804384747d15_r.jpg -> 49ce58f2c038c709968a804384747d15_r.jpg
        local_path = "/Users/y/PythonWorkSpace/" + img[img.rindex("/") + 1:len(img)]
        urllib.urlretrieve(img, local_path)

    return
