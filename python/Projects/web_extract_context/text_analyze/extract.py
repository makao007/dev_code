#coding:utf-8

import urllib
import urllib2
import urlparse
import re
from math import ceil,sqrt,log

def remove_js_css (content):
    """ remove the the javascript and the stylesheet content (<script>....</script> and <style>....</style>) """
    r = re.compile(r'''<script.*?</script>''',re.I|re.M|re.S)
    s = r.sub ('',content)

    r = re.compile(r'''<style.*?</style>''',re.I|re.M|re.S)
    s = r.sub ('', s)

    return s


def remove_multi_space (content):
    """remove multi space """
    r = re.compile(r'''^\s+''',re.S|re.M)
    s = r.sub ('', s)
    return s.replace('\r','').replace('\n','').replace('&nbsp;',' ')

def remove_any_tag (s):
    s = re.sub(r'''<[^>]+>''','',s)
    return s.strip()

def split_by_tag_a (content):
    if not content:
        return ''
    return re.split(r'''<\s*/\s*a\s*>''',content)

def split_by_newline (content):
    if not content:
        return ''
    return content.split('\n')

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

def is_context_edge (data,mean):
    avg = float(sum(data))/len(data)
    if avg < mean:
        return True
    else:
        return False
        

def find_context_pos (line_text_length):
    if not line_text_length:
        return [0,0]

    w1 = 0.2
    w2 = 0.8
    avg_k = 3
    result = []

    for i in range(len(line_text_length)):
        t = line_text_length[i]
        # (  the length of the text in <a> * weight 1  +   the rest length of the text in whole line * weight 2  ) /  number of tags
        tmp = (t[1]*w1) + (t[2]-t[1])*w2  

        result.append (tmp)
        #print '%4d %4d %4d %4d' % (i,t[0],t[1],t[2])

    # assume the content always with the longest text line
    max_index = result.index(max(result))
    mean = (sum (result)+0.0) / len (result)

    #find the left edge position
    i = max_index
    while i > 1:
        if result[i] < mean and is_context_edge (result[i-avg_k:i+avg_k],mean):
            break
        i = i - 1

    #find the right edge position
    j = max_index
    while j < len (result)-1:
        if result[j] < mean and is_context_edge (result[j-avg_k:j+avg_k],mean):
            break
        j = j + 1
    
    write_file (','.join(map (str, result)), 'data')
    write_file (','.join(map (str, line_text_length)), 'data_line')
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


def tag_article (s):
    if "<article" in s.lower():
        content = re.findall(r'''<article.*?</article>''',s,re.I|re.M|re.S)
        if content:
            return content[0]
    return ''

def extract_context (url):
    web_page = fetch (url)
    #article = tag_article (web_page)
    #if article:
    #    return article
    lines = split_by_tag_a(remove_html_tag(web_page))
    [l,r] = find_context_pos(compute_line_length (lines))
    if l ==0 and r == 0:
        return 'Sorry, some <b>Error</b> happend in the page : %s' % url
    else:
        return '</a>\n'.join(lines[l:r]) + "</a>"


def find_content_position (content):
    pass

def find_content_position_known (content,start_partern, end_partern):
    start_index = content.index(start_partern)
    end_index   = content.index(end_partern)
    start_line  = content[:start_index].count('\n')
    end_line    = content[:end_index  ].count('\n')

    return start_line, end_line, start_index, end_index


