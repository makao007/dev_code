#!/usr/bin/python  
#coding=utf-8  
  
import gzip
import urllib  
import urllib2  
import StringIO
import cookielib  

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

def post(url,data, url2):
    request = urllib2.Request(url)
    for k,v in header_dict().iteritems():
        request.add_header(k,v)
    data = urllib.urlencode(data)
    response = urllib2.urlopen(request, data)

    cookies = response.headers["Set-cookie"]

    request = urllib2.Request(url2)
    for k,v in header_dict().iteritems():
        request.add_header(k,v)
    request.add_header('Cookie', cookies)
    response = urllib2.urlopen(request, data)

    if response.info().get('content-encoding','') == 'gzip' or response.info().get('Content-Encoding', '') == 'gzip':
        return gzip.GzipFile(fileobj=StringIO.StringIO(response.read())).read()
    else:
        return response.read()

def write_file (filename, content):
    w = open(filename,'w')
    w.write(content)
    w.close()

def main():  
    url1 = 'https://reg.163.com/logins.jsp'
    url2 = 'http://reader.youdao.com/view.do?_=138259703662&method=viewChannel&param=4134975263908880489&pageIndex=1&first=0&viewnew=0&viewtitle=1&shot=-1'
    input_url="http://account.youdao.com/login?service=reader&amp;back_url=http%3A%2F%2Freader.youdao.com%2Fview.do%3Fmethod%3DviewChannel%26pageIndex%3D249%26param%3D4134975263908880489%26first%3D0%26viewtitle%3D1%26shot%3D-1%26viewnew%3D0%26_%3D1382592916423&amp;success=1"

    username = "makao009@126.com"
    password = "newnet204618007"

    data = {"url":input_url, "product":"search", "type":"1", "username":username,"password":password}

    s = post(url1, data,url2)  
    write_file ('a.html',s)
  
if __name__ == '__main__':  
    main()

