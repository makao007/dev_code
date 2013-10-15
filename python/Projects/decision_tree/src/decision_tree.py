#coding=utf-8
import os
import math
import string
import operator


def load_dataset (filename="a.txt"):
    return map(string.split,file(filename).readlines())

def split_dataset(dataset, value,column):
    sub_dataset = []
    for line in dataset:
        if line[column] != value:
            continue
        else:
            sub_dataset.append (line[:column] + line[column+1:])
    return sub_dataset


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
    base_info_gain = dataset_entropy (dataset)

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

        if (base_info_gain-entropy) > max_info_gain_value :
            max_info_gain_value = base_info_gain - entropy
            max_info_gain_index = i

    return max_info_gain_index
        
def which_class (dataset,with_percentage=False):
    if not dataset:
        return None
    labels = {}
    for line in dataset:
        key = line[-1]
        if not labels.has_key (key):
            labels[key] = 0
        labels[key] += 1

    labels_sorted = sorted (labels.iteritems(), key=operator.itemgetter(1), reverse=True)    
    if with_percentage:
        return labels_sorted[0][0], float(labels_sorted[0][1])/len(dataset)
    else:
        return labels_sorted[0][0]


def make_tree (dataset,feature_names,with_percentage=False):
    labels =  [line[-1] for line in dataset] 
    if labels.count(labels[0]) == len (labels):
        return labels[0],1.0
    if len (dataset[0]) == 1:
        return which_class (dataset,with_percentage)

    max_index = max_info_gain (dataset)

    max_feature = feature_names.pop(max_index)

    sub_tree = {max_feature:{}}

    values = set([line[max_index] for line in dataset])
    for value in values:
        tmp = split_dataset(dataset,value,max_index)
        sub_tree[max_feature][value] = make_tree(tmp, feature_names,with_percentage)
    return sub_tree

def d_tree (dataset, feature_names=[],with_percentage=False):
    if not dataset:
        raise Exception('the dataset is null')

    if not feature_names:
        feature_names = range(len(dataset[0])-1)

    return make_tree(dataset,feature_names,with_percentage)

def print_dict (d,n=0):
    for k,v in d.items():
        print '\t'*n,
        if type(v)==type({}):
            print "%s : {" % k
            print_dict(v,n+1)
        else:
            print("%s : %s" % (k,v))

    if n!=0:
        print '\t'*(n-1)+ '}'


def _test_entropy ():
    feature_names = ['no surfacing','flippers']
    dataset1 = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
    dataset1.append ([1,1,'yes'])
    dataset1.append ([1,1,'yes'])
    dataset1.append ([1,1,'no'])

    dataset2 = load_dataset()
    #print dataset_entropy (dataset1)
    #print dataset_entropy (dataset2)

    print_dict (d_tree (dataset1,feature_names,True))
    print '==========================='
    print_dict (d_tree (dataset2,[],True))

_test_entropy()



