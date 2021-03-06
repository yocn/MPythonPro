#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2, time, bs4, ssl, os, urllib

locol = "/Users/y/PythonWorkSpace/se0343/text/"
locolPic = "/Users/y/PythonWorkSpace/se0343/pic/"

index = 1  # 范围1~28  下载到 8 9
picUrlIds = (9, 10, 11, 12, 13, 14, 39)
picurl = "https://www.se0343.com:2087/news-show-id-%s-p-%s.html" % (8, index)
url = "https://www.se0343.com:2087/news-show-id-12-p-28.html"
textUrl = "https://www.se0343.com:2087/news-read-id-10795.html"
picUrl = "https://www.se0343.com:2087/news-read-id-10488.html"

picBaseUrl = "https://www.se0343.com:2087"

testPic = "https://www.se0343.com:2087/Uploads/images/xqcbjkia/346911.jpg"


class Pic:
    def __init__(self, url, desc, path):
        self.url = url
        self.desc = desc
        self.path = path


def test():
    # download_text(textUrl)
    # downSinglePic(testPic, "te.jpg")
    # download_pic(picUrl, 1)
    # analyzingTextUrl()
    analizingPic()
    return


def analyzingTextUrl():
    # 分类[40,47] index[1-28]
    for i in range(40, 48):
        currentDir = locol + str(i) + "/"
        if not os.path.exists(currentDir):
            os.mkdir(currentDir)
        for j in range(1, 29):
            url = "https://www.se0343.com:2087/news-show-id-%d-p-%d.html" % (i, j)
            getTxtPageUrl(currentDir, url, i, j)


def getTxtPageUrl(rootDir, txtListUrl, i, j):
    baseTextUrl = "https://www.se0343.com:2087"
    webheader = {
        'Accept': 'text/html, application/xhtml+xml, */*',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'DNT': '1',
        'Connection': 'Keep-Alive',
        'Host': 'www.se0343.com'
        # 'Host': 'www.douban.com'
    }

    context = ssl._create_unverified_context()
    req = urllib2.Request(url=txtListUrl, headers=webheader)
    response = urllib2.urlopen(req, context=context)

    if response.code != 200:
        return
    html = response.read().decode('utf-8')
    if html.strip() == '':
        return
    soup = bs4.BeautifulSoup(html, "html.parser", from_encoding="utf-8")
    asa = soup.find_all("a")
    for a in asa:
        if not a.get('title') == None:
            href = a['href']
            realHref = baseTextUrl + href
            # print realHref
            download_text(rootDir, realHref.encode("utf-8"), i, j)


def download_text(rootDir, url, i, j):
    print "开始执行Task 下载文本文件 %s  i:%s  j:%s" % (url, i, j)
    webheader = {
        'Accept': 'text/html, application/xhtml+xml, */*',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'DNT': '1',
        'Connection': 'Keep-Alive',
        'Host': 'www.se0343.com'
        # 'Host': 'www.douban.com'
    }

    context = ssl._create_unverified_context()
    req = urllib2.Request(url=url, headers=webheader)
    response = urllib2.urlopen(req, context=context)

    if response.code != 200:
        return
    html = response.read().decode('utf-8')
    if html.strip() == '':
        return
    soup = bs4.BeautifulSoup(html, "html.parser", from_encoding="utf-8")

    h1s = soup.find_all("h1")
    for h1 in h1s:
        if "class" in h1.attrs:
            if 'text-overflow' in h1.attrs['class']:
                title = h1.contents[0]
                fileName = rootDir + title + ".txt"
                print fileName

    divs = soup.find_all("div")
    for div in divs:
        # print div.attrs
        # class ="details-content text-justify"
        if "class" in div.attrs:
            if 'details-content' in div.attrs['class']:
                content = str(div.contents[1])
                # print content
                real = content.replace('<br/><br/>', '\n').replace("</p>", "").replace("<p>", "")
                # print real
                try:
                    with open(fileName, 'w') as f:  # 设置文件对象
                        f.write(str(real))
                        print '写入成功，休息一下，休息1s'
                except IOError:
                    print "Error: 没有找到文件或读取文件失败"

    time.sleep(1)
    return


def analizingPic():
    picUrlIds = (9, 10, 11, 12, 13, 14, 39)
    for id in picUrlIds:
        currentDir = locolPic + str(id) + "/"
        if not os.path.exists(currentDir):
            os.mkdir(currentDir)
        for index in range(7, 29):
            picurl = "https://www.se0343.com:2087/news-show-id-%s-p-%s.html" % (id, index)
            getPicPicUrl(currentDir, picurl, id, index)


def getPicPicUrl(rootDir, pic_url, i, j):
    print pic_url, i, j
    baseTextUrl = "https://www.se0343.com:2087"
    webheader = {
        'Accept': 'text/html, application/xhtml+xml, */*',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'DNT': '1',
        'Connection': 'Keep-Alive',
        'Host': 'www.se0343.com'
        # 'Host': 'www.douban.com'
    }

    context = ssl._create_unverified_context()
    req = urllib2.Request(url=pic_url, headers=webheader)
    response = urllib2.urlopen(req, context=context)

    if response.code != 200:
        return
    html = response.read().decode('utf-8')
    if html.strip() == '':
        return
    soup = bs4.BeautifulSoup(html, "html.parser")
    asa = soup.find_all("a")
    for a in asa:
        if not a.get('title') == None:
            href = a['href']
            title = a['title']
            titleDir = rootDir + title + "/"
            titleDir = titleDir.encode("utf-8")
            if not os.path.exists(titleDir):
                os.mkdir(titleDir)
            realHref = baseTextUrl + href
            # print realHref
            download_pic(titleDir, realHref.encode("utf-8"), i, j)
    time.sleep(0.3)


def download_pic(rootDir, url, i, j):
    if not os.path.exists(rootDir):
        os.mkdir(rootDir)
    print "下载图片目录 %s  url:%s %d %d" % (rootDir, url, i, j)
    webheader = {
        'Accept': 'text/html, application/xhtml+xml, */*',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'DNT': '1',
        'Connection': 'Keep-Alive',
        'Host': 'www.se0343.com'
        # 'Host': 'www.douban.com'
    }

    context = ssl._create_unverified_context()
    req = urllib2.Request(url=url, headers=webheader)
    response = urllib2.urlopen(req, context=context)

    if response.code != 200:
        return
    html = response.read().decode('utf-8')
    if html.strip() == '':
        return
    soup = bs4.BeautifulSoup(html, "html.parser")
    pic_list = []

    h1s = soup.find_all("h1")
    for h1 in h1s:
        if "class" in h1.attrs:
            if 'text-overflow' in h1.attrs['class']:
                title = h1.contents[0]
                fileName = rootDir + title.encode("utf-8") + ".jpg"
                print fileName

    imgs = soup.find_all("img")
    for img in imgs:
        if "src" in img.attrs:
            ii = img.attrs['src']
            realPicUrl = picBaseUrl + ii

            realPicUrl = realPicUrl.encode("utf-8")
            desc = realPicUrl[-10: -4]
            realFileName = fileName[0:-4] + desc + ".jpg"
            # fileName = fileName.encode("utf-8")
            pic = Pic(realPicUrl,
                      desc,
                      realFileName)
            # print pic.url + " " + pic.path + " " + pic.desc
            pic_list.append(pic)

    for pic in pic_list:
        downSinglePic(pic.url, pic.path)


def downSinglePic(url, name):
    print url, name
    webheader = {
        'Accept': 'text/html, application/xhtml+xml, */*',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'DNT': '1',
        'Connection': 'Keep-Alive',
        'Host': 'www.se0343.com'
        # 'Host': 'www.douban.com'
    }

    context = ssl._create_unverified_context()
    req = urllib2.Request(url=url, headers=webheader)
    f = urllib2.urlopen(req, context=context)

    data = f.read()
    with open(name, "wb") as code:
        code.write(data)
