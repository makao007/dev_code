#coding=utf-8

import re
import urlparse
from fetch import *



def sina_sub_rss_url (url):
    template = r'''<a href="(http://rss.sina.com.cn/[^\.]+.xml)" class="f14"><font color="#000000">([^<]+)</font></a>'''
    return sina_fetch(url, template)

def sina_sub_category_rss():
    index = 'http://rss.sina.com.cn/index.shtml'
    template = r'''<a href="([^"]+)" class="a02">([^<]+)</a>'''
    return sina_fetch(index, template)

def sina_fetch (index, template):
    content = fetch (index)
    urls = re.findall(template, content)
    result = []
    for url in urls:
        result.append ([urlparse.urljoin(index,url[0]),url[1]])
    return result

def show_sina_rss ():
    urls = sina_sub_category_rss()
    for url in urls:
        print '------------------'
        print url[1]
        xmls = sina_sub_rss_url(url[0])
        for xml in xmls:
            print xml[1],xml[0]

show_sina_rss()

