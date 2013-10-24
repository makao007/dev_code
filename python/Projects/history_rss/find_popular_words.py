#-*- coding:utf-8 -*-

import operator
import sys

def top_k_words (s,n):
    sign = '、 。 ， ： “ ” ？ 》 《 ！ , " ! . '.decode('utf8').split(' ')
    sign.extend ([u' ',u'\n',u'\r','\t'])

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
   
    i = 0
    result = []
    for k,v in words_sorted:
        if i>n :
            break
        i += 1
        result.append ((k,v))
    return result

def test_top_k_works():

    s = '''
经过整理，笔者共筛选了500多个关键词，如：转会、队长、传奇、名单、大将、赞、新星、对手、训练、国脚、锋霸、点球、VS、主场、天王等等。这些关键词的筛选，笔者筛选关键词的依据主要有以下几点：

l  与体育活动相关，可是场外或者场内

l  属于日常用语，不能造词

l  需要是通过词汇，即具有普适性，比如像“贝克汉姆带儿子逛街”就不作为关键词，因为其他球员出现类似情况的概率很低。

l  尽可能多的找，然后整理。比如“小小罗”和”C罗”是同一个人，但是笔者将其作为两个关键词。'''
    s = s.decode('utf8')
    for i in top_k_words(s,10):
        print i[0],i[1],len(i[0])

test_top_k_works()





