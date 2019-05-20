#!/usr/bin/python
# -*- coding: UTF-8 -*-
from InfoBean import *


def create(conn):
    # 注意 CREATE TABLE 这种语句不分大小写
    sql_create = '''
    create table if not exists `data` (
        `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        `name`    TEXT NOT NULL UNIQUE,
        `url`    TEXT NOT NULL,
        `status`    INTEGER,
        `path`    TEXT,
        `desc`    TEXT
    )
    '''
    # 用 execute 执行一条 sql 语句
    conn.execute(sql_create)
    # print('创建成功')


def insert(conn, name, url, status, path, desc):
    sql_insert = '''
    INSERT INTO
        data(name, url, status, path, desc)
    VALUES
        (?, ?, ?, ?, ?);
    '''
    conn.execute(sql_insert, (name, url, status, path, desc))
    print 'insert插入数据成功', name, url, status, path, desc


def insert_info(conn, info):
    exist_info = select(conn, info.name)
    if exist_info is None:
        insert(conn, info.name, info.url, info.status, info.path, info.desc)
    else:
        update(conn, info.name, info.url, info.status, info.path, info.desc)


def select(conn, name):
    # 一个注入的用户名
    sql = '''
    SELECT
        *
    FROM
        data
    WHERE 
        name = ?
    '''
    # 这是读取数据的套路
    cursor = conn.execute(sql, (name,))
    info = None
    for row in cursor:
        print row[0], row[1], row[2], row[3], row[4], row[5]
        info = InfoBean(row[0], row[1], row[2], row[3], row[4], row[5])
        print info
    print 'select数据', info
    return info


def delete(conn, user_id):
    sql_delete = '''
    DELETE FROM
        data
    WHERE
        id = ?
    '''
    # 注意, execute 的第二个参数是一个 tuple
    # tuple 只有一个元素的时候必须是这样的写法
    conn.execute(sql_delete, (user_id,))


def update(conn, name, url, status, path, desc):
    sql_update = '''
    UPDATE
        `data`
    SET
        `name`=?,`url`=?,`status`=?,`path`=?,`desc`=?
    WHERE
        `name`=?
    '''
    conn.execute(sql_update, (name, url, status, path, desc, name))
    print 'update数据', name, url, status, path, desc
