#!/usr/bin/python
# -*- coding: UTF-8 -*-

def test():
    a = 1
    while a < 7:
        if (a % 2 == 0):
            print(a, "偶数")
        else:
            print(a, "基数")

        a += 1

    b = 10
    if (b >= 0 and b <= 5) or (b >= 10 or b <= 15):
        print(b, "b")

    return
