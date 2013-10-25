#-*- coding:utf-8 -*-

import operator
import sys
import os

def top_k_words (s,n):
    sign = '、 。 ， ： “ ” ？ 》 《 ！ , " ! . （ ） ( ) & # ￥ $'.decode('utf8').split(' ')
    sign.extend ([u' ',u'\n',u'\r',u'\t',u'\\'])
    sign.extend (map(str,range(10)))

    words = {}
    length = 0
    
    for i in range(len(s)-1):
        if s[i] in sign or s[i+1] in sign:
            continue
        word = s[i:i+2]
        if not words.has_key (word):
            words[word] = 0
        words[word] += 1
        length += 1
    words_sorted = sorted (words.iteritems(), key=operator.itemgetter(1), reverse=True)   
   
    return words_sorted[:n],length


def read_file_from_json (dir_name):
    if not os.path.isdir(dir_name):
        print 'the folder not exists', dir_name
        return 
    files = os.listdir(dir_name)
    content = ''
    for filename in files:
        info = eval (file(os.path.join(dir_name,filename)).read())
        for article in info.get('articles'):
            content += article.get('title') + '\n' + article.get('desc') + '\n'

    content = content.decode('utf8')
    return content

def test_top_k_works():

    s = '''
经过整理，笔者共筛选了500多个关键词，如：转会、队长、传奇、名单、大将、赞、新星、对手、训练、国脚、锋霸、点球、VS、主场、天王等等。这些关键词的筛选，笔者筛选关键词的依据主要有以下几点：

l  与体育活动相关，可是场外或者场内

l  属于日常用语，不能造词

l  需要是通过词汇，即具有普适性，比如像“贝克汉姆带儿子逛街”就不作为关键词，因为其他球员出现类似情况的概率很低。

l  尽可能多的找，然后整理。比如“小小罗”和”C罗”是同一个人，但是笔者将其作为两个关键词。'''
    s = s.decode('utf8')

    dir_name = 'E:/Data/youdao_rss/4134975263908880489'
    s = read_file_from_json(dir_name)
    for i in top_k_words(s,100)[0]:
        print i[0],i[1],len(i[0])

test_top_k_works()





