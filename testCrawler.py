#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2
import urllib
import bs4
from bs4 import BeautifulSoup


def test():
    url = "https://zhuanlan.zhihu.com/p/65551350"
    response1 = urllib2.urlopen(url)
    # print response1.read()
    # print response1.getcode()

    html = """
    <html>
    <head><title>The Dormouse's story</title></head>
    <body>
    <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class="story">...</p>
    """

    html_doc = ""
    soup = bs4.BeautifulSoup(html, "html.parser", from_encoding="utf-8")
    # print soup.prettify()
    # print soup.p
    # print soup.title()
    # print soup.head()
    # links = soup.find_all('title')
    # print "所有的链接", links
    # https://blog.csdn.net/love666666shen/article/details/77512353
    print "soup.title->", soup.title
    print "soup.title.name->", soup.title.name
    print "soup.title.string->", soup.title.string
    print "soup.title.parent.name->", soup.title.parent.name
    print "soup.p->", soup.p
    print "soup.p['class']->", soup.p['class']
    print "soup.a['href']->", soup.a['href']
    # 修改第一个 a 标签的href属性为 http://www.baidu.com/
    soup.a['href'] = 'http://www.baidu.com/'

    ##输出第一个  p 标签的所有子节点
    print soup.p.contents

    # 输出第一个  a 标签
    print soup.a

    # 输出所有的  a 标签，以列表形式显示
    print soup.find_all('a')

    # 输出第一个 id 属性等于  link3 的  a 标签
    print soup.find(id="link3")

    # 获取所有文字内容
    print(soup.get_text())

    return
