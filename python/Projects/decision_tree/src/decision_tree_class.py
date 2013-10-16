#coding=utf-8

from decision_tree import *

import pickle
import os

class D_tree :
    def __init__ (self, tree_filename=None):
        self.tree = None
        self.feature = None
        self.tree_key = 'tree'
        self.feature_key = 'feature'
        self.with_percentage = True
        if tree_filename is not None:
            self.load_tree (tree_filename)

    def set_with_percentage (self,f):
        if type (f) != type (True):
            print 'Data type Error, the type must be Boolean (True or False)'
            return 
        self.with_percentage = f

    def set_feature (self, names):
        """ the feature names """
        self.feature = names

    def make_tree (self,data):
        if type(data) == type(''):   #filename
            dataset = load_dataset(data)
        elif type(data) == type ([]):  #list, dataset
            dataset = data
        else:
            raise Exception('dataset type not reconigze')

        self.tree = d_tree (dataset,[],self.with_percentage)


    def _load_tree (self, tree_filename):
        if os.path.isfile (tree_filename):
            try:
                r = open (tree_filename)
                tmp = pickle.load (r)
            except:
                print 'load data error : %s' % tree_filename
            finally:
                r.close()
            return tmp
        else:
            print 'filename %s not exists' % tree_filename

    def load_tree (self, tree_filename):
        tmp = self._load_tree (tree_filename)
        self.tree = tmp.get(self.tree_key)
        self.feature = tmp.get(self.feature_key)

    def show_tree (self, tree_filename=None):
        if tree_filename is not None:
            show_dict (_load_tree (tree_filename).get(self.feature_key))
            show_dict (_load_tree (tree_filename).get(self.tree_key))
        else:
            show_dict (self.feature)
            show_dict (self.tree)

    def save_tree (self, filename="tree.dat"):
        w = open (filename,'w')
        pickle.dump ({self.tree_key:self.tree, self.feature_key: self.feature}, w)
        w.close()

    def clear_tree (self):
        self.tree = {}

    def show_dict (self,data):
        print_dict (data)

    def fill_tree (self,sub_tree):
        """ fill the feature name """
        if not self.feature:
            return sub_tree
        if type(sub_tree) != type ({}):
            return sub_tree 
        key,value = sub_tree.items()[0]
        new_key = self.feature[key]
        tmp = {new_key:{}}
        for k,v in value.items():
            tmp[new_key][k] = self.fill_tree (v)
        return tmp


    def _classify (self, features, sub_tree):
        if type (sub_tree) != type ({}):
            return sub_tree
        else:
            key,value = sub_tree.items()[0]
            for k,v in value.items():
                if features[key] == k:
                    return self._classify (features, v)
            
            print 'no found'
            return None


    def classify (self, features):
        if not self.tree :
            print 'the tree is empty'
            return None
        
        return self._classify(features,self.tree)
            



