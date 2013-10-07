#coding:utf-8

import urllib
import urlparse
import re
from math import ceil
import os

def fetch (url):
    return urllib.urlopen(url).read()

def remove_html_tag (content):
    r = re.compile(r'''<script.*?</script>''',re.I|re.M|re.S)
    s = r.sub ('',content)

    r = re.compile(r'''<style.*?</style>''',re.I|re.M|re.S)
    s = r.sub ('', s)

    r = re.compile(r'''<[^>]+>''',re.S|re.M)
    s = r.sub ('', s)

    r = re.compile(r'''^\s+''',re.S|re.M)
    s = r.sub ('', s)

    r = re.compile(r'''^\n+''',re.S|re.M)
    s = r.sub('\n', s)

    return s.replace('&gt;','>').replace('&lt;','<').replace('\r','').replace('&nbsp;',' ')

def group_block_text (content, k=3):
    #group k lines into one line
    lines =content.split('\n')
    return [' '.join(lines[i*k:i*k+k]) for i in range(int(ceil(float(len(lines))/k)))]

def compute_line_length (content):
    return [len(line) for line in content]

def find_context_pos (line_length):
    text_sum = sum (line_length)
    text_max = max (line_length)
    text_len = len (line_length)

    x1 = 0.25
    x2 = 0.1
    x3 = 0.7


    tmp = map (lambda x: 1 if x >x1*text_max else 0, line_length)
    pos_left = tmp.index(1)
    try:
        for i in range (text_len):
            if sum (tmp[i:int(i+x2*text_len)]) >= int(x2*text_len*x3):
                pos_left = i
                break
    except:
        print 'error'
        print tmp
    for i in range(pos_left,text_len):
        pos_right = i
        if sum (tmp[i:int(i+x2*text_len)])==0:
            break
    return [pos_left,pos_right] 
    
def write_file (s,filename):
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

def extract_context (url):
    s = remove_html_tag(fetch(url))
    gs = group_block_text(s,1)
    [l,r] = find_context_pos(compute_line_length (gs))
    write_file ('\n'.join(gs[l:r]), os.path.split(urlparse.urlparse(url)[2])[1])


for url in file('urls.txt'):
    extract_context(url.strip())
