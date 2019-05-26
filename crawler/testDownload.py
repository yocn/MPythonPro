import urllib2
import ssl

url = "https://www.se0343.com:2087/Uploads/images/xqcbjkia/346910.jpg"

webheader = {
    'Accept': 'text/html, application/xhtml+xml, */*',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'DNT': '1',
    'Connection': 'Keep-Alive',
    'Host': 'www.se0343.com'
    # 'Host': 'www.douban.com'
}

context = ssl._create_unverified_context()
req = urllib2.Request(url=url, headers=webheader)
f = urllib2.urlopen(req, context=context)

data = f.read()
with open("a.jpg", "wb") as code:
    code.write(data)
