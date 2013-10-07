#coding:utf-8

import urllib
import urlparse
import re
import os
import time

def fetch (url):
    content = urllib.urlopen(url).read()
    return content

def find_url(url,param):
    content = fetch(url)
    urls = re.findall(param,content)
    return urls

def show_url (urls):
    for i,url in enumerate(urls):
        print i,url
    return urls

def write_url (urls,filename='urls.txt'):
    w = open(filename,'w+')
    w.writelines('\n'.join(urls))
    w.close()

def find_match(urls,param,with_title=False):
    result = []
    for url in urls:
        content = fetch(url)
        temp = re.findall(param,content,re.S|re.M|re.I)
        for i in temp:
            if with_title:
                full_url = urllib.unquote(urlparse.urljoin(url,i[0]))
                result.append ([full_url,i[1]])
            else:
                full_url = urllib.unquote(urlparse.urljoin(url,i))
                result.append (full_url)
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
        print 'downloading file %s' % url
        filename = urllib.unquote(os.path.split(urlparse.urlparse(url)[2])[1])
        dirname  = urllib.unquote(dirname)
        filepath = os.path.join(dirname,filename)
        timestamp = time.strftime("%Y-%m-%d %H-%M-%S  ", time.localtime())
        try:
            if os.path.isfile(filepath) and exist_skip:
                down_urls.append ("%s %10s %s" % (timestamp, 'exists', url)) 
            else:
                urllib.urlretrieve(url,filepath)
                down_urls.append ("%s %10s %s" % (timestamp, 'download', url))
                succ_urls.append (timestamp + url)
        except:
            timestamp = time.strftime("%Y-%m-%d %H-%M-%S  ", time.localtime())
            down_urls.append ("%s %10s %s" % (timestamp, 'fail', url)) 
            fail_urls.append (timestamp + url)
    write_url (succ_urls, os.path.join(dirname,succ_log))
    write_url (fail_urls, os.path.join(dirname,fail_log))
    write_url (down_urls, os.path.join(dirname,download_log))

def make_url(template_url):
    num = re.findall(r'''\{\{(\d+)-(\d+)\}\}''',template_url)
    tem = re.findall(r'''([^\{]+)\{\{\d+-\d+\}\}(.+)''',template_url)
    if num and tem:
        result = []
        for i in range(int(num[0][0]),int(num[0][1])+1):
            result.append ( tem[0][0] + str(i) + tem[0][1] )
    return result


def start_download (urls,rules,tag, debug_mode=False):

    if not rules:
        print urls, rules
        for url in urls:
            if debug_mode:
                show_url ([url])
            download_to_local ([url],tag)
    else:
        for url in urls:
            urlset = find_match ([url],rules[0])
            start_download (urlset, rules[1:], tag)


