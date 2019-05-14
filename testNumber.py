#!/usr/bin/python
# -*- coding: UTF-8 -*-

def test():
    # --------------------------String----------------------
    a = 0
    b = 1
    b += 1
    c = a + b
    d = a - b
    e = abs(d)
    f = (d == e)
    g = bin(12).replace("0b", "")  # 采用 python 自带了方法 bin 函数，比如 bin(12345) 回返回字符串 '0b11000000111001', 这个时候在把0b去掉即可

    print a, b, c, d, e, f, g
    return
