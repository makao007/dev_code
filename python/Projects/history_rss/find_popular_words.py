#coding=utf-8

import operator
import sys
import os
import codecs
import string

def merge_dict (d1,d2):
    for k in d2:
        if d1.has_key (k):
            d1[k] += d2[k]
        else:
            d1[k] = d2[k]

def top_k_words (s,n=100):
    sign = '、 。 ， ： “ ” ？ 》 《 ！ , " ! . （ ） ( ) & # ￥ $ ; / [ ]'.decode('utf8').split(' ')
    sign.extend ([u' ',u'\n',u'\r',u'\t',u'\\'])
    sign.extend (map(str,range(10)))
    sign.extend (list(string.ascii_letters))

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
   
    return words,length


def read_json (filename):
    if not os.path.isfile (filename):
        print 'file not exists', filename
        return 
    info = eval (file(filename).read())
    content = ''
    for article in info.get('articles'):
        content += article.get('title') + '\n' + article.get('desc') + '\n'
    content = content.decode('utf8')
    return content

def group_key_word (dir_name, n=20):
    if not os.path.isdir (dir_name):
        print 'folder not exists', dir_name
        return 
    key_words = {}
    words_length = 0

    for root,dirs,files in os.walk (dir_name):
        print root
        for filename in files:
            tmp = top_k_words (read_json(os.path.join (root, filename)))
            merge_dict (key_words, tmp[0])
            words_length += tmp[1]

    words_sorted = sorted (key_words.iteritems(), key=operator.itemgetter(1), reverse=True)   
   
    static_filename = dir_name.replace('/','_').replace('\\','_') + '_' + str(n)+ '_statics.txt'
    w = codecs.open(static_filename, "w", "utf-8")
    for k,v in words_sorted[:n]:
        w.write ('%s %d\n' % (k,v))
    w.close()



if __name__ == "__main__":
    group_key_word ('data/房产新闻'.decode('utf8'),500)
