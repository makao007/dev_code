#coding=utf-8

import urllib
import urllib2
import urlparse
import re
import os
import time

from fetch import fetch

def find_url(url,param):
    content = fetch(url)
    urls = re.findall(param,content)
    return urls

def show_url (urls):
    for i,url in enumerate(urls):
        print i,url
    return urls

def write_url (urls,filename='urls.txt'):
    w = open(filename,'a+')
    w.write('\n'.join(urls))
    w.close()

def find_match(urls,param):
    result = []
    for url in urls:
        content = fetch(url)
        param2 = ''
        if type(param)==type(''): 
            param1 = param
        elif type(param) == type([]):
            param1 = param[0]
            param2 = param[1]

        #find the regular match url
        temp = re.findall(param1,content,re.S|re.M|re.I)
        for i in temp:
            result.append( urllib.unquote(urlparse.urljoin(url,i)) )

        #find the "brother" match url
        if param2:
            temp = re.findall(param2, content,re.S|re.M|re.I)
            print 'find param2',param2
            print temp
            for i in temp:
                next_url = urllib.unquote(urlparse.urljoin(url,i))
                result.extend(find_match ([next_url],param))

    return result


def download_to_local(urls,dirname='',exist_skip=True,succ_log='succ_download.log',fail_log='fail_download.log',download_log='download.log'):
    if dirname == '':
        dirname = time.strftime("%Y-%m-%d__%H-%M-%S", time.localtime())
    if not os.path.isdir(dirname):
        os.mkdir(dirname)

    succ_urls = []
    fail_urls = []
    down_urls = []
    for url in urls:
        url = url.replace(r'\/','/')
        print 'downloading file %s' % url
        filename = urllib.unquote(os.path.split(urlparse.urlparse(url)[2])[1])
        dirname  = urllib.unquote(dirname)
        filepath = os.path.join(dirname,filename)
        timestamp = time.strftime("%Y-%m-%d %H-%M-%S  ", time.localtime())
        status_msg = ""
        try:
            if os.path.isfile(filepath) and exist_skip:
                status_msg = 'exists'
            else:
                urllib.urlretrieve(url,filepath)          #download the file to local PC
                status_msg = 'download'
                succ_urls.append ("%s %s\n" % (timestamp, url))
        except IOError:
            status_msg = 'fail'
            fail_urls.append ("%s %s\n" % (timestamp,url) )
        down_urls.append ("%s %10s %s\n" % (timestamp, status_msg, url)) 
    write_url (succ_urls, os.path.join(dirname,succ_log))
    write_url (fail_urls, os.path.join(dirname,fail_log))
    write_url (down_urls, os.path.join(dirname,download_log))

def make_url(template_url):
    if '{{' not in template_url:
        return [template_url]
    num = re.findall(r'''\{\{(\d+)-(\d+)\}\}''',template_url)
    tem = re.findall(r'''([^\{]+)\{\{\d+-\d+\}\}(.*)''',template_url)
    result = []
    if num and tem:
        for i in range(int(num[0][0]),int(num[0][1])+1):
            result.append ( tem[0][0] + str(i) + tem[0][1] )
    return result


def start_download (urls,rules,tag, debug_mode=False):

    if not rules:
        for url in urls:
            if debug_mode:
                show_url ([url])
            download_to_local ([url],tag)
    else:
        for url in urls:
            urlset = find_match ([url],rules[0])
            start_download (urlset, rules[1:], tag)


