#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import math
import testCondition

def test():
    content = dir(testCondition)
    # print dir(testCondition)
    for index in range(len(content)):
        print(index, "-", content[index])
    print globals().keys()
    print locals().keys()
    return
