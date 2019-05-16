#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys, os, stat


def test():
    print "sys.argv->", sys.argv
    print sys.stdout
    print sys.path
    print sys.platform
    # 执行shell
    # fd = os.open("exe.sh", os.O_RDWR)
    # os.fchmod(fd, stat.S_IXOTH)
    # os.system("./exe.sh")

    os.system("chmod 777 exe.sh;./exe.sh")

    return
