#coding:utf-8

import urllib
import urllib2
import urlparse
import re
from math import ceil,sqrt,log


def std (data):
    temp = 0
    mean = (sum (data) + 0.0) / len (data)
    for i in data:
        temp += pow(i-mean,2)  
    return temp / len (data)

def fetch (url):
    timeout_second = 10
    request = urllib2.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.69 Safari/537.36')
    try:
        response = urllib2.urlopen(request, timeout=timeout_second)
        if response.code == 200:
            s = response.read()
        else:
            s = ''
        try:
            return s.decode('gbk').encode('utf8')
        except:
            return s
    except:
        ''

def remove_html_tag (content):
    if not content:
        return ''
    r = re.compile(r'''<script.*?</script>''',re.I|re.M|re.S)
    s = r.sub ('',content)

    r = re.compile(r'''<style.*?</style>''',re.I|re.M|re.S)
    s = r.sub ('', s)

    r = re.compile(r'''^\s+''',re.S|re.M)
    s = r.sub ('', s)

    return s.replace('\r','').replace('\n','').replace('&nbsp;',' ')
    #s.replace('&gt;','>').replace('&lt;','<')

def remove_any_tag (s):
    s = re.sub(r'''<[^>]+>''','',s)
    return s.strip()

def split_by_tag_a (content):
    return re.split(r'''<\s*/\s*a\s*>''',content)

def compute_line_length (lines):
    result = []

    #write_file ('</a>\n'.join(lines),'aa.html')
    for line in lines:
        line = line.lower()
        tag_num = line.count('<') - line.count('<br')
        if '<a' in line:
            tmp = line.rindex('<a')        
            text_num = len(remove_any_tag (line[tmp:]))
        else:
            text_num = 0
        char_num = len(remove_any_tag (line))

        result.append ([ tag_num, text_num, char_num] )

    return result

def find_context_pos (line_text_length):
    w1 = 0.2
    w2 = 0.5
    ws = [0.1,0.2,0.3]
    result = []
    with_author = True
    with_ws_avg = True  # use previous k average value

    for i in range(len(line_text_length)):
        t = line_text_length[i]
        # (  the length of the text in <a> * weight 1  +   the length of the text in whole line * weight 2  ) /  number of tags
        tmp = (t[1]*w1 + (t[2]-t[1])*w2) / (t[0]+1)

        if with_ws_avg and i > len(ws):
            temp = 0
            for ii in range(len(ws)):
                tt = line_text_length[i-len(ws)+ii]
                temp += ws[ii] * (tt[1]*w1 + (tt[2]-tt[1])*w2) / (tt[0]+1)
            temp = temp / sum(ws)

            tmp = tmp * 0.4 + temp * 0.6

        result.append (tmp)
        #print '%4d %4d %4d %4d' % (i,t[0],t[1],t[2])

    max_index = result.index(max(result))
    mean = (sum (result)+0.0) / len (result)

    #find the left position
    i = max_index
    while i > 1:
        if result[i] < mean:
            if result[i-1] > result[i]:
                break
        i = i - 1

    #find the right position
    j = max_index
    while j < len (result):
        if  result[j] < mean:
            if result[j+1] > result[j]:
                break
        j = j + 1
    
    #match the author and publish date infomation
    if with_author :
        while i > 1:
            if result[i-1] < result[i]:
                break
            i = i -1 
    write_file (','.join(map (str, result)), 'data')
    return [i,j]

def write_file (s,filename):
    import os
    if 'SERVER_SOFTWARE' in os.environ:
        return 
    if not filename:
        import time 
        filename = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    default_dir = 'context'
    if not os.path.isdir (default_dir):
        os.mkdir(default_dir)
    filename = 'context' + os.path.sep + filename + '.txt'
    w = open(filename,'w')
    w.write(s)
    w.close()

def extract_content (url):
    lines = split_by_tag_a(remove_html_tag(fetch(url)))
    [l,r] = find_context_pos(compute_line_length (lines))
    if l ==0 and r == 0:
        return 'no content of this page'
    else:
        return '</a>\n'.join(lines[l:r]) + "</a>"

