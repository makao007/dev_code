#!/usr/bin/python  
#coding=utf-8  
  
import os
import re
import gzip
import time
import urllib  
import urllib2  
import StringIO
import cookielib  

from fetch import *

def write_file (filename, content):
    w = open(filename,'w')
    w.write(content)
    w.close()

def timestamp ():
    return str(time.time()).replace('.','')


def youdao_xml_to_id (xml_url, cookie):
    url = "http://reader.youdao.com/subscribe.do?_=%s1&method=addChannel&addChannel=%s&page=1" % (timestamp(),urllib.quote(xml_url,''))
    template = r'''<span class="btnR" onclick="YSubMgr.subFeed\('([^']+)'\);"><span class="sprite">\+</span>订阅</span>'''

    try:
        content = fetch (url,None,cookie)
    except urllib2.HTTPError:
        return ''
    except urllib2.URLError:
        return ''
    xml_id = re.findall (template, content)
    if len(xml_id)>=1:
        return xml_id[0]
    else:
        print 'Error, get xml id fail'
        return ''

def youdao_login_get_cookie ():
    url = 'https://reg.163.com/logins.jsp'
    input_url="http://account.youdao.com/login?service=reader&amp;back_url=http%3A%2F%2Freader.youdao.com%2Fview.do%3Fmethod%3DviewChannel%26pageIndex%3D249%26param%3D4134975263908880489%26first%3D0%26viewtitle%3D1%26shot%3D-1%26viewnew%3D0%26_%3D1382592916423&amp;success=1"
    username = "makao009@126.com"
    password = "newnet204618007"
    data = {"url":input_url, "product":"search", "type":"1", "username":username,"password":password}
    s,c = fetch(url, data,None, True)  
    return c

def youdao_get_rss_records(xml_id,cookie, start_page=1, end_page=251, parent_dir='./'):
    url = 'http://reader.youdao.com/view.do?_=%s&method=viewChannel&param=%s&pageIndex=%d&first=0&viewnew=0&viewtitle=1&shot=-1'
    for i in range(start_page, end_page):
        try:
            url = url % (timestamp(), xml_id, i)
        except:
            print xml_id,i
        s = fetch (url,None, cookie)
        s = s.replace('true','True').replace('false','False')

        filename = os.path.join(parent_dir,str(i)+'.json')
        write_file (filename,s)
        print 'page %d ' % i


def load_rss_source (local_filename=''):
    info = {}
    if local_filename and os.path.isfile (local_filename):
        content = file (local_filename).read()
        groups  = content.split('------------------\n')
        for group in groups:
            line = group.strip().split('\n')
            xmls = []
            for i in range(1,len(line)-1):
                tmp = line[i].strip().split(' ')
                xmls.append (tmp)
            info[line[0]] = xmls
        return info
    else:
        print 'please input type RSS source file '
        return 
        


def youdao_xml_ids():  
    info = load_rss_source('sina_rss.txt')
    cookie = youdao_login_get_cookie ()
    content = ''
    for k,v in info.iteritems():
        content += '------------------\n%s\n' % k
        for value in v:
            xml_id = youdao_xml_to_id (value[1],cookie)
            if not xml_id:
                xml_id = "None"
            content += "%s %s %s\n" % (value[0], value[1], xml_id)

    write_file ('sina_rss_id.txt',content)
    
def main ():
    #youdao_xml_ids()
    cookie = youdao_login_get_cookie ()
    info = load_rss_source('sina_rss_id.txt')
    for k,v in info.iteritems():
        dir_name = os.path.join("data",k)
        if not os.path.isdir(dir_name):
            os.mkdir (dir_name)
        for i in v:
            if i[2] == 'None':
                continue
            sub_dir_name = os.path.join(dir_name,i[0])
            if not os.path.isdir(sub_dir_name):
                os.mkdir (sub_dir_name)

            youdao_get_rss_records(i[2],cookie, parent_dir=sub_dir_name)



if __name__ == '__main__':  
    main()

