#encoding=utf-8

import find_popular_words
import tf_idf

class TextClassification :

    def __init__ (self):
        self.info = None

    def save_top_words (self,dir_name='key_words'):
        if self.info is None:
            print 'Error, the training set infomation is empty, please load training dataset first'
            return 
        find_popular_words.save_top_words(self.info, dir_name)
        
    def save_info_file (self, filename):
        if self.info is None:
            print 'Error, he training set infomation is empty, please load training dataset first'
            return 
        print 'create new infomation file to', filename
        tf_idf.save_info (self.info, filename)

    def load_info_file (self, filename):
        self.info = tf_idf.load_info (filename)

    def get_category_text (self,article):
        if self.info is None or not article:
            print 'Error, the training set infomation is empty, please load training dataset first'
            return 

        return tf_idf.category (self.info, article)

    def train_dataset (self, filename, n=4000):
        """ load the training dataset infomation file """
        self.info = find_popular_words.group_key_word (filename,n)








