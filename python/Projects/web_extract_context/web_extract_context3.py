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

    r = re.compile(r'''^\s+''',re.S|re.M)
    s = r.sub ('', s)

    return s.replace('\r','').replace('\n','').replace('&nbsp;',' ')
    #s.replace('&gt;','>').replace('&lt;','<')

def remove_any_tag (s):
    s = re.sub(r'''<[^>]+>''','',s)
    return s.strip()

def compute_line_length (content):
    result = []
    lines = re.split(r'''<\s*/\s*a\s*>''',content)

    #write_file ('</a>\n'.join(lines),'aa.html')
    for line in lines:
        line = line.lower()
        tag_num = line.count('<')
        if '<a' in line:
            tmp = line.rindex('<a')        
            text_num = len(remove_any_tag (line[tmp:]))
        else:
            text_num = 0
        char_num = len(remove_any_tag (line))

        result.append ([ tag_num, text_num, char_num] )

    return result

def find_context_pos (line_text_length):
    w1 = 0.3
    w2 = 0.5
    result = []
    for i in range(len(line_text_length)):
        t = line_text_length[i]
        # (  the length of the text in <a> * weight 1  +   the length of the text in whole line * weight 2  ) /  number of tags
        tmp = (t[1]*w1 + (t[2]-t[1])*w2) / t[0]
        result.append (tmp)
        #print '%4d %4d %4d %4d' % (i,t[0],t[1],t[2])

    write_file (','.join(map (str, result)), 'data')
    
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
    find_context_pos(compute_line_length (s))


for url in file('a.txt'):
    extract_context(url.strip())
