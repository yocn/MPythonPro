#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time

def test():
    # --------------------------String----------------------
    var1 = 'Hello World!'
    var2 = "Python Runoob"

    a = var1 + var2  # 字符串连接
    b = var1 * 2  # 字符串连接
    c = var1[1]  # 通过索引获取字符串中字符
    d = var1[1:3]  # 截取字符串中的一部分
    e = "ll" in var1  # 成员运算符 - 如果字符串中包含给定的字符返回 True
    f = "x" not in var1  # 成员运算符 - 如果字符串中不包含给定的字符返回 True
    g = '\n'
    h = 'r\n'  # 原始字符串
    i = "My name is %s and weight is %d kg!" % ("John", 21)
    j = '''Hi
    change Line'''  # 换行
    print(a, b, c, d, e, f, g, h, i, j)

    i = 10
    print i * 2
    print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    return
