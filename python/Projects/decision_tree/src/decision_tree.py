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
    columns = len (dataset[0]) -1 
    length = len (dataset)

    max_info_gain_index = -1
    max_info_gain_value = -1
    for i in range (columns):
        features = [line[i] for line in dataset]
        features_dict = {}
        for feature in features:
            if not features_dict.has_key(feature):
                features_dict[feature] = 0
            features_dict[feature] += 1

        entropy = 0
        for key,value in features_dict.items():
            entropy += float(value)/length * dataset_entropy(dataset, key, i)

        if entropy > max_info_gain_value :
            max_info_gain_value = entropy
            max_info_gain_index = i

    return max_info_gain_index
        

def _test_entropy ():
    dataset1 = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
    dataset2 = load_dataset()
    print dataset_entropy (dataset1)
    print dataset_entropy (dataset2)

    print max_info_gain (dataset2)

_test_entropy()







