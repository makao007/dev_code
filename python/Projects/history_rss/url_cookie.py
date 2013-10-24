#!/usr/bin/python
#coding:utf-8
import urllib,urllib2,cookielib


def header_dict ():
    chrome_header = '''
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding:gzip,deflate,sdch
Accept-Language:en-US,en;q=0.8,zh-CN;q=0.6
Cache-Control:max-age=0
Connection:keep-alive
Host:reader.youdao.com
User-Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'''
    
    header = {}
    for line in chrome_header.strip().split('\n'):
        header[line.split(':',1)[0]] = line.split(':',1)[1]
    return header

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

username = "makao009@126.com"
password = "newnet204618007"

url1 = 'https://reg.163.com/logins.jsp'
url2 = 'http://reader.youdao.com/view.do?_=1382592920469&method=viewChannel&param=4134975263908880489&pageIndex=247&first=0&viewnew=0&viewtitle=1&shot=-1'

input_url="http://account.youdao.com/login?service=reader&amp;back_url=http%3A%2F%2Freader.youdao.com%2Fview.do%3Fmethod%3DviewChannel%26pageIndex%3D249%26param%3D4134975263908880489%26first%3D0%26viewtitle%3D1%26shot%3D-1%26viewnew%3D0%26_%3D1382592916423&amp;success=1"

data = {"url":input_url, "product":"search", "type":"1", "username":username,"password":password}
url_data = urllib.urlencode(data)

request = urllib2.Request(url1)
for k,v in header_dict().iteritems():
    print '%s: %s' % (k,v)
    request.add_header(k,v)

url_open = urllib2.urlopen(request,url_data)
if url_open:
    start = urllib2.urlopen(url2,url_data)
    if start:
        print start.read().decode('utf').encode('gbk')
    else:
        print "done"

