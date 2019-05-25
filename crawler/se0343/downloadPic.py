#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2, urllib, os, time, bs4, ssl

locol = "/Users/y/PythonWorkSpace/se0343/"

index = 1  # 范围1~28
picUrlIds = (8, 9, 10, 11, 12, 13, 14, 39)
picurl = "https://www.se0343.com:2087/news-show-id-%s-p-%s.html" % (8, index)
url = "https://www.se0343.com:2087/news-show-id-12-p-28.html"
textPic = "https://www.se0343.com:2087/news-read-id-10795.html"


def test():
    download_text(textPic)
    return


def download_text(url):
    print "开始执行Task %s" % url
    context = ssl._create_unverified_context()
    request = urllib2.Request(url)  # Request参数有三个，url,data,headers,如果没有data参数，那就得按我这样的写法
    request.add_header("User-Agent",
                       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36")
    request.add_header("Accept-Language", "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,fr;q=0.6")
    request.add_header("Accept",
                       "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3")

    response = urllib2.urlopen(request, context=context)
    if response.code != 200:
        return
    html = response.read()
    if html.strip() == '':
        return
    soup = bs4.BeautifulSoup(html, "html.parser", from_encoding="utf-8")

    divs = soup.find_all("div")
    for div in divs:
        print div
        # class ="details-content text-justify"
        print div.attrs
    # dict = json.loads(html, encoding="?GBK")
    # print raw.keys()
    # print dict[u'picInfo']
    # pic_list = []
    # pic_info = dict[u'picInfo']
    # current_dir = locol + "" + str(index) + "/"
    # for info in pic_info:
    #     source = info[u'source']
    #     desc = info[u'add_intro']
    #     suffix = '.gif'
    #     if source.endswith("gif"):
    #         suffix = '.gif'
    #     elif source.endswith("jpg"):
    #         suffix = '.jpg'
    #     else:
    #         return
    #     path = current_dir + desc + suffix
    #     pic = Pic(source, desc, path)
    #     pic_list.append(pic)
    #
    # for pic in pic_list:
    #     if not os.path.exists(current_dir):
    #         os.mkdir(current_dir)
    #     print "-------------开始下载---------------", pic.url, pic.path
    #     urllib.urlretrieve(pic.url, pic.path)

    print '休息一下，休息3s'
    time.sleep(3)
    return
