import urllib2
import ssl

# weburl="https://www.se0343.com:2087"
weburl="https://www.se0343.com:2087/news-read-id-10795.html"
# weburl = "https://www.douban.com/"
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
req = urllib2.Request(url=weburl, headers=webheader)
webPage = urllib2.urlopen(req, context=context)
data = webPage.read().decode('utf-8')
print data
print type(data)
print type(webPage)
print webPage.geturl()
print webPage.info()
print webPage.getcode()
