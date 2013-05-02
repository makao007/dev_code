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
    w = open(filename,'w')
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
        timestamp = time.strftime("%Y-%m-%d %H-%M-%S  ", time.localtime())
        try:
            if os.path.isfile(filename) and exist_skip:
                down_urls.append ("%s %10s %s" % (timestamp, 'exists', url)) 
            else:
                urllib.urlretrieve(url,os.path.join(dirname,filename))
                down_urls.append ("%s %10s %s" % (timestamp, 'download', url))
                succ_urls.append (timestamp + url)
        except:
            timestamp = time.strftime("%Y-%m-%d %H-%M-%S  ", time.localtime())
            down_urls.append ("%s %10s %s" % (timestamp, 'fail', url)) 
            fail_urls.append (timestamp + url)
    write_url (succ_urls, succ_log)
    write_url (fail_urls, fail_log)
    write_url (down_urls, download_log)

def make_url(template_url):
    num = re.findall(r'''\{\{(\d+)-(\d+)\}\}''',template_url)
    tem = re.findall(r'''([^\{]+)\{\{\d+-\d+\}\}(.+)''',template_url)
    if num and tem:
        result = []
        for i in range(int(num[0][0]),int(num[0][1])+1):
            result.append ( tem[0][0] + str(i) + tem[0][1] )
    return result




#------------------------------------
#template_url = 'http://www.pingshu8.com/Musiclist/mmc_220_348_{{1-10}}.htm'
#param1 = r'''<li class="a1">[^<]+<a href=["']([^"']+)' target='_blank'>[^>]+</a></li>'''
#urls = ['http://www.pingshu8.com/Musiclist/mmc_220_348_1.htm']
#show_url(make_url(template_url))
#show_url(find_match(make_url(template_url),param1))
#download_to_local(find_match(find_match(urls,param1),param2))
#write_url(show_url(find_match(find_match(urls,param1), param2)))
#download_to_local(['http://pl1.pingshu8.com:8000/ps/%D5%C5%D4%C3%BF%AC_%D0%A1%C0%EE%B7%C9%B5%B6%D4%C1%D3%EF/%D5%C5%D4%C3%BF%AC_%D0%A1%C0%EE%B7%C9%B5%B6%D4%C1%D3%EF_010.mp3?11302557604378x1367418367x11302563383120-a0dff5439f134ac374768c2912c3f19b'])

'''
http://www.pingshu8.com/play_67178.html
http://www.pingshu8.com/MusicList/mmc_221_1082_1.Htm
http://www.ysts8.com/play_1033_46_1_1.html
http://www.ysts8.com/Yshtml/Ys1033.html
'''
#------------------------------------
