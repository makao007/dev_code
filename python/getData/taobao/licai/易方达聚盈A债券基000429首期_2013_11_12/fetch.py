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
        User-Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'''
    header = {}
    for line in chrome_header.strip().split('\n'):
        header[line.strip().split(':',1)[0]] = line.split(':',1)[1]
    return header

def fetch (url, data=None, cookies=None, get_cookie=False):
    timeout  = 10
    request = urllib2.Request(url)
    for k,v in header_dict().iteritems():
        request.add_header(k,v)
    if cookies is not None:
        request.add_header('Cookie', cookies)
    try:
        if data:
            data = urllib.urlencode(data)
            response = urllib2.urlopen(request, data, timeout)
        else:
            response = urllib2.urlopen(request, timeout=timeout)
        pass
    except IOError :
        print 'Error when download %s' % url
        print 
        return ''

    if response.info().get('content-encoding','') == 'gzip' or response.info().get('Content-Encoding', '') == 'gzip':
        content = gzip.GzipFile(fileobj=StringIO.StringIO(response.read())).read()
    else:
        content = response.read()

    if get_cookie:
        return content, response.headers["Set-cookie"]
    else:
        return content
