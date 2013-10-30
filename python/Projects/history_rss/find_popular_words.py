#encoding=utf-8

import os
import re
import sys
import codecs
import string
import operator

import read_write_file
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

def make_info_statics_file (info,dir_name):
    for group_name,group_words in info:
        content = []
        words_sorted = sorted (group_words.iteritems(), key=operator.itemgetter(1), reverse=True)   
        i=0
        for k,v in words_sorted:
            content.append ('%s %d' % (k,v))
            i += 1
        filename = group_name + '_' + str(i)+ '_statics.txt'
        filename = os.path.join (dir_name, filename)
        read_write_file.write (filename, '\n'.join(content))


def group_key_word (info_filename, n=20):
    """ the parameter n mean how many top n words should be save """

    group_dir = {}
    for line in file (info_filename):
        line = line.strip().decode('utf8')
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
        
        if n==-1:
            group_dir[group_name] = same_group_key_words
        else:
            words_sorted = sorted (same_group_key_words.iteritems(), key=operator.itemgetter(1), reverse=True)   
            group_dir[group_name] = dict (words_sorted[:n])

    return group_dir


if __name__ == "__main__":
    if len (sys.argv)!=2:
        print 'Usage :  text file'
        exit(1)
    if not os.path.isfile (sys.argv[1]):
        print 'file not exists %s ' % sys.argv[1]
    group_key_word (sys.argv[1],4000)
