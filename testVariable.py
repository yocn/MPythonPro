#!/usr/bin/python
# -*- coding: UTF-8 -*-

def test():
    # --------------------------String----------------------
    counter = 100  # 赋值整型变量
    miles = 1000.0  # 浮点型
    hello = "Hello! "  # 字符串
    helloworld = "Hello World!"  # 字符串

    print counter
    print miles
    print helloworld
    print helloworld[0:6]
    print helloworld[6:]
    h = helloworld[1:4]
    print "h-----------------> " + h
    print "h[:2]-------------> " + h[:2]
    print "helloworld[1:4:2]-> " + helloworld[1:4:2]

    # --------------------------Python列表-------------------------
    list = ['a', 1, 22, 'b']
    list2 = ['c', 100, 222, "d"]
    print list
    print list[:2]
    print list2
    print list2 * 2
    print list + list2

    # --------------------------Python元组，相当于只读列表-------------------------
    tuple = ('aaa', 70, "ssss", 99)
    print tuple

    # --------------------------Python字典-------------------------
    print("--------------------------Python字典-------------------------")
    dict = {}
    dict['one'] = "One Dict"
    dict[2] = "Two Dict"
    dict['3'] = "Three Dict"
    dict2 = {"AOne": 'AOne', "BOne": "BOne"}
    print dict
    print dict.keys()
    print dict.values()
    print dict['3']
    # print "dict2->" + dict2.keys()+ "   value2->" + dict2.values()
    print dict2
    print 'dict2[\'AOne\']->' + dict2['AOne']

    # --------------------------Python数据类型转换-------------------------
    print("--------------------------Python数据类型转换-------------------------")
    i10 = int('121', 10)
    i2 = int('1111', 2)  # 1111当做2进制转化成10进制
    print(i10)
    print(i2)
    print(type(i10))
    print(isinstance(i10, int))

    return
