#encoding=utf-8

import os
import re
import sys
import codecs
import string
import operator

import split_article_into_words

def merge_dict (d1,d2):
    for k in d2:
        if d1.has_key (k):
            d1[k] += d2[k]
        else:
            d1[k] = d2[k]


def read_json (filename):
    if not os.path.isfile (filename):
        print 'file not exists', filename
        return 
    try:
        info = eval (file(filename).read())
    except:
        print 'Error parse file', filename
        return ''
    content = ''
    for article in info.get('articles'):
        content += article.get('title') + '\n' + article.get('desc') + '\n'
    content = content.decode('utf8')
    return content


def group_key_word (info_filename, n=20):
    """ the parameter n mean how many top n words should be save """

    group_dir = {}
    for line in file (info_filename):
        line = line.strip()
        if not line:
            continue

        tmp = re.split (r'\s+',line)
        group_name = tmp[0]
        dir_name = tmp[1]
        if not group_dir.has_key (group_name):
            group_dir[group_name] = []
        group_dir[group_name].append (dir_name)

    for group_name,dir_names in group_dir.iteritems():
        same_group_key_words = {}
        same_group_words_length = 0
        for dir_name in dir_names:

            if not os.path.isdir (dir_name):
                print 'Error, folder not exists %s' % dir_name
                continue

            for root,dirs,files in os.walk (dir_name):
                print root
                for filename in files:
                    tmp = split_article_into_words.split_text(read_json(os.path.join (root, filename)))
                    merge_dict (same_group_key_words, tmp[0])
                    same_group_words_length += tmp[1]

        words_sorted = sorted (same_group_key_words.iteritems(), key=operator.itemgetter(1), reverse=True)   
        static_filename = group_name + '_' + str(n)+ '_statics.txt'

            w = codecs.open(static_filename, "w", "utf-8")
            for k,v in words_sorted[:n]:
                w.write ('%s %d\n' % (k,v))
            w.close()



if __name__ == "__main__":
    if len (sys.argv)!=2:
        print 'Usage : %s filename ' % sys.argv[0]
        exit(1)
    if not os.path.isfile (sys.argv[1]):
        print 'file not exists %s ' % sys.argv[1]
    group_key_word (sys.argv[1],4000)
