#coding=utf-8

import os
import pickle
import operator

import find_popular_words
from read_write_file import *


def load_files (dir_name):
    files = os.listdir (dir_name)
    words_info = {}
    for filename in files:
        if filename == 'README.txt':
            continue
        full_filename = os.path.join(dir_name, filename)
        if os.path.isfile (full_filename):
            name = filename.split('_')[0]

        tmp = {}
        length = 0
        for line in read(full_filename).strip().split('\n'):
            temp = line.split(' ')
            tmp[temp[0].lower()] = int(temp[1])
            length += int(temp[1])
        tmp['total'] = length

        words_info[name] = tmp

    return words_info


def top_k_word_bayes (info, k=100, need_sort=True):
    info_bayes= {}

    for key,value in info.iteritems():
        for word, times  in value.iteritems():
            p = float (times) / (info[key]['total']) 
            if info_bayes.has_key (word):
                info_bayes[word] += 1.0
            else:
                info_bayes[word] = 1.0

    
    result = {}
    for key,value in info.iteritems():
        tmp = {}
        for word, times  in value.iteritems():
            p = float (times) / (info[key]['total']) / info_bayes[word] 
            #p = float (times) / (info[key]['total']) 
            tmp[word] = p
        if need_sort:
            result[key] = sorted (tmp.iteritems(), key=operator.itemgetter(1), reverse=True) [:k] 
        else:
            result[key] = tmp
    return result

def show_top_k_words (info,k=100):
    for key,value in info.iteritems():
        print '----------------'
        print key
        for i in range(k):
            try:
                print value[i][0],value[i][1]
            except:
                print 'error'
                err.append (value[i][0])


def category (info,content):
    article_info,length = find_popular_words.top_k_words(content)
    max_value = 0
    out_match = 1.0
    category_text = ''

    for key,value in info.iteritems():
        tmp = 0
        tmp2 = 0
        for word in article_info:
            if value.has_key (word):
                tmp += value[word] * article_info[word]/length
            else:
                tmp2 += 1
        if tmp > max_value:
            category_text = key
            max_value = tmp
            out_match = tmp2

    return category_text,max_value,out_match


def save_info (info,filename):
    w = open(filename,'w')
    pickle.dump (info,w)
    w.close()

def load_info (filename):
    r = open(filename,'r')
    info = pickle.load(r)
    r.close()
    return info

def make_info_file (dir_name,filename):
    info =top_k_word_bayes(load_files(dir_name),-1,False)
    save_info (info,filename)
    print 'make info file successful, save in',filename

if __name__ == "__main__":
    #show_top_k_words (top_k_word_bayes(load_files ('keywords'),-1),30)
    make_info_file('keywords','info.dat')

    #info = load_info()
    #test_category ('testset', info)
