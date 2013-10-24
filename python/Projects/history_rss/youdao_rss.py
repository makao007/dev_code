#coding=utf-8

import time
import urllib2

def header_dict ():
    chrome_header = '''
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding:gzip,deflate,sdch
Accept-Language:en-US,en;q=0.8,zh-CN;q=0.6
Cache-Control:max-age=0
Connection:keep-alive
Cookie:OUTFOX_SEARCH_USER_ID=-1340503200@113.103.11.33; NTES_SESS=JfJhBKdU8c73W0WcLJ6Mxe.P6TdsDvfhFL7.pvBMcGNheJ2XDeA2YGixdRZVHd_D_TQRPQGnS_kdfSq.6_NRR6slvyk.4cOxgU1RjoX7UurDnlHEKkg_cEtSelXqdW1.tNGQEFfwYYTGtn0lGPiCe3o4e; ANTICSRF=12a1d43bf247968b7ff2c0230f0759bb; S_INFO=1382592647|0|#3&40#|makao009@126.com#makao007@126.com#makao008@126.com; P_INFO=makao009@126.com|1382592647|0|search|11&25|gud&1382584375&mail126#gud&440100#10#0#0|&0|mail126_chg&search&mail126&blog|makao009@126.com; SESSION_FROM_COOKIE=unknown; JSESSIONID=abcai5orrbQJza5qz8Ohu; viewtitle=1; viewsummary=0; viewnew=0
Host:reader.youdao.com
User-Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'''
    
    header = {}
    for line in chrome_header.strip().split('\n'):
        header[line.split(':',1)[0]] = line.split(':',1)[1]
    return header


def fetch (url):
    try:
        timeout_second = 20
        if not url.lower().startswith('http'):
            url = 'http://' + url
        request = urllib2.Request(url)
        for k,v in header_dict().iteritems():
            print '%s: %s' % (k,v)
            request.add_header(k,v)
        response = urllib2.urlopen(request, timeout=timeout_second)
        content = response.read()
    except IOError:
        print 'Error download %s fail ' % url
        return ''

def make_youdao_rss_url (source, page):
    timestamp = str(time.time()).replace('.','')
    url = 'http://reader.youdao.com/view.do?_=%s&method=viewChannel&param=%s&pageIndex=%d&first=0&viewnew=0&viewtitle=1&shot=-1'
    url = url % (timestamp, source, page)
    return url

def test_fetch ():
    print fetch(make_youdao_rss_url ('4134975263908880489',1))

test_fetch()

