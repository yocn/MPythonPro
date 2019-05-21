#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sqlite3
from SQLiteHelper import *
from InfoBean import *
from random import *


def test():
    # 指定数据库名字并打开
    db_path = 'test.sqlite'
    conn = sqlite3.connect(db_path)
    # print("打开了数据库")
    # 打开数据库后 就可以用 create 函数创建表
    create(conn)
    for i in range(8, 18):
        info = InfoBean(0, "name" + str(i), "url" + str(randint(0, 100)), "status", "path", "desc")
        insert_info(conn, info)

    # info1 = select(conn, "name1")
    # info2 = select(conn, "name")
    # print info1, info2
    #
    # 必须用 commit 函数提交你的修改
    # 否则你的修改不会被写入数据库
    conn.commit()
    # 用完数据库要关闭
    conn.close()
    return
