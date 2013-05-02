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

def find_match(urls,param):
    result = []
    for url in urls:
        content = fetch(url)
        temp = re.findall(param,content,re.S|re.M|re.I)
        for i in temp:
            result.append (urllib.unquote(urlparse.urljoin(url,i)))
    return result

def download_to_local(urls,dirname=''):
    if dirname == '':
        dirname = time.strftime("%Y-%m-%d__%H-%M-%S", time.localtime())
    if not os.path.isdir(dirname):
        os.mkdir(dirname)

    succ_urls = []
    fail_urls = []
    for url in urls:
        print 'downloading file %s' % url
        filename = urllib.unquote(os.path.split(urlparse.urlparse(url)[2])[1])
        try:
            urllib.urlretrieve(url,os.path.join(dirname,filename))
            succ_urls.append (url)
        except:
            fail_urls.append (url)
    write_url (succ_urls,'succ_urls.txt')
    write_url (fail_urls,'fail_urls.txt')

def make_url(template_url):
    num = re.findall(r'''\{\{(\d+)-(\d+)\}\}''',template_url)
    tem = re.findall(r'''([^\{]+)\{\{\d+-\d+\}\}(.+)''',template_url)
    if num and tem:
        result = []
        for i in range(int(num[0][0]),int(num[0][1])+1):
            result.append ( tem[0][0] + str(i) + tem[0][1] )
    return result


template_url = 'http://www.pingshu8.com/Musiclist/mmc_220_348_{{1-10}}.htm'
template_url = 'http://www.pingshu8.com/MusicList/mmc_221_1079_{{1-13}}.Htm'
param1 = r'''<li class="a1">[^<]+<a href=["']([^"']+)' target='_blank'>[^>]+</a></li>'''
param2 = r'''<param name="URL" value="([^"]+)">'''
download_to_local(show_url(find_match(find_match(make_url(template_url),param1), param2)))

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
