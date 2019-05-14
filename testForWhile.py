#!/usr/bin/python
# -*- coding: UTF-8 -*-

def test():
    # --------------------------String----------------------
    fruit = ['bana', 'apple', 'bear']
    for letter in 'apple':
        print 'shuiguo->', letter
    for f in fruit:
        print 'shuiguo->', f
    for index in range(len(fruit)):
        print 'ss->', index, fruit[index]

    for index in range(10, 20):
        if index == 13:
            break
        print 'ss->', index
    return
