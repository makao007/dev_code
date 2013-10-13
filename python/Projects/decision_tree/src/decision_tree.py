#coding=utf-8
import os
import math
import string


def load_dataset (filename="a.txt"):
    return map(string.split,file(filename).readlines())

def entropy (labels,length):
    if length == 0:
        raise ValueError('the length of dataset could not be empty')
    entropy = 0
    for line in labels:
        p = float(labels[line]) / length
        entropy -= math.log(p,2) * p

    return entropy


def dataset_entropy (dataset, value=None, column=None):
    if not dataset:
        return 
    dataset_length = len (dataset)

    labels = {}
    for line in dataset:
        if value is not None :
            if line[column] != value:
                continue
        key = line[-1]
        if not labels.has_key(key):
            labels[key] = 0
        labels[key] += 1
    return entropy (labels, dataset_length)

def max_info_gain (dataset):
    

def _test_entropy ():
    print dataset_entropy([[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']])
    print dataset_entropy (load_dataset())

_test_entropy()







