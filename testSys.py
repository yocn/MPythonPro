#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import os


def test():
    print "sys.argv->", sys.argv
    print sys.stdout
    print sys.path
    print sys.platform
    # 执行shell
    os.system("chmod 777 exe.sh;./exe.sh")
    return
