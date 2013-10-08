#coding:utf-8

import urllib
import urlparse
import re
from math import ceil

def fetch (url):
    return urllib.urlopen(url).read()

def remove_html_tag (content):
    r = re.compile(r'''<script.*?</script>''',re.I|re.M|re.S)
    s = r.sub ('',content)

    r = re.compile(r'''<style.*?</style>''',re.I|re.M|re.S)
    s = r.sub ('', s)

    r = re.compile(r'''^\s+''',re.S|re.M)
    s = r.sub ('', s)

    r = re.compile(r'''^\n+''',re.S|re.M)
    s = r.sub('\n', s)
    return s.replace('&gt;','>').replace('&lt;','<').replace('\r','').replace('&nbsp;',' ')


def compute_line_length (content):
    r = re.compile(r'''<[^>]+>''',re.S|re.M)
    result = []
    for line in content.split('\n'):
        line = line.strip()
        text = r.sub ('', line)
        line_length = len (line)
        text_length = len (text)
        if line_length == 0:
            line_length = 1
        result.append ([line_length,text_length])
    return result

def find_context_pos (line_text_length):
    pos_left  = 0
    pos_right = 0

    tmp_pos_left = 0

    max_text_rate = 0
    min_text_rate = 1

    tmp = 0
    tmps = []
    position = []
    for i in range (len(line_text_length)):
        #tmp = tmp + (line_text_length[i][0]-2.0*line_text_length[i][1]) / line_text_length[i][0]
        tmp = tmp + (line_text_length[i][0]-2.0*line_text_length[i][1]) 
        #print '%4d %4d %4d %4.2f' % (i,line_text_length[i][0],line_text_length[i][1],tmp)
        tmps.append (tmp)
        if tmp > max_text_rate :
            max_text_rate = tmp
            min_text_rate = tmp
            pos_left = i

        if tmp < min_text_rate :
            min_text_rate = tmp
            pos_right = i
            position.append ([pos_left,pos_right, abs(tmps[pos_right]-tmps[pos_left])])

    #write_file(','.join(map(str,tmps)),'')
    distance_value = 0
    distance_index = 0
    for j in range(len(position)):
        tmp = position[j][2]
        if tmp > distance_value:
            distance_value = tmp
            distance_index = j
    
    if not position :
        return [0,0]
    else:
        return [position[distance_index][0], position[distance_index][1]+1]


def extract_context (url):
    s = remove_html_tag(fetch(url))
    [l,r] = find_context_pos(compute_line_length (s))
    return '\n'.join(s.split('\n')[l:r])

