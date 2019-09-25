#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
https://sm.ms/doc/v2
1、上传 https://sm.ms/api/v2/upload
返回格式
{
    "success": true,
    "code": "success",
    "message": "Upload success.",
    "data": {
        "file_id": 0,
        "width": 934,
        "height": 1401,
        "filename": "write.jpg",
        "storename": "wbduF4hjN5R2H3e.jpg",
        "size": 98342,
        "path": "/2019/09/25/wbduF4hjN5R2H3e.jpg",
        "hash": "RkgV6Ejyuh9FOCwopxK7ZJYL2B",
        "url": "https://i.loli.net/2019/09/25/wbduF4hjN5R2H3e.jpg",
        "delete": "https://sm.ms/delete/RkgV6Ejyuh9FOCwopxK7ZJYL2B",
        "page": "https://sm.ms/image/wbduF4hjN5R2H3e"
    },
    "RequestId": "F209CD87-B0FD-412A-834D-1287EB5B3568"
}

"""

import requests

def uploadImage(path):
    url = 'https://sm.ms/api/v2/upload'
    headers = {
        'Content-Type': 'multipart/form-data',
        'Authorization': 't4YruMCm3e0S6cNwR8aQIrp6msOrMcQY'
    }
    file = open('QR.png', 'rb')
    # file = open('/Users/yocn/Documents/GitHub/MPythonPro/un.jpg', 'rb')
    print(file.name)
    files = {'smfile': file}
    res = requests.post(url=url, headers=headers, files=files)
    print(res.text)

    return
