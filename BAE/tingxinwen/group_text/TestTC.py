#encoding=utf-8

import os
import TextClassification
import find_popular_words

tc = TextClassification.TextClassification()
tc.load_info_file('info.dat')


testing_dataset =[ 
'体育新闻','E:\dev\git\dev_code\python\Projects\history_rss\data\体育新闻',
'军事新闻','E:\dev\git\dev_code\python\Projects\history_rss\data\军事新闻',
'女性新闻','E:\dev\git\dev_code\python\Projects\history_rss\data\女性新闻',
'明星娱乐','E:\dev\git\dev_code\python\Projects\history_rss\data\娱乐新闻',
'房产新闻','E:\dev\git\dev_code\python\Projects\history_rss\data\房产新闻',
'文化教育','E:\dev\git\dev_code\python\Projects\history_rss\data\文化教育',
'时尚新闻','E:\dev\git\dev_code\python\Projects\history_rss\data\时尚新闻',
'星座新闻','E:\dev\git\dev_code\python\Projects\history_rss\data\星座新闻',
'汽车新闻','E:\dev\git\dev_code\python\Projects\history_rss\data\汽车新闻',
'游戏新闻','E:\dev\git\dev_code\python\Projects\history_rss\data\游戏新闻',
'科技新闻','E:\dev\git\dev_code\python\Projects\history_rss\data\科技新闻',
'育儿指导','E:\dev\git\dev_code\python\Projects\history_rss\data\育儿指导',
'读书新闻','E:\dev\git\dev_code\python\Projects\history_rss\data\读书新闻',
'财经新闻','E:\dev\git\dev_code\python\Projects\history_rss\data\财经新闻',
'国内要闻','E:\dev\git\dev_code\python\Projects\history_rss\data\新闻中心\国内要闻',
'百姓生活','E:\dev\git\dev_code\python\Projects\history_rss\data\新闻中心\社会万象',
'百姓生活','E:\dev\git\dev_code\python\Projects\history_rss\data\新闻中心\社会新闻',
'百姓生活','E:\dev\git\dev_code\python\Projects\history_rss\data\新闻中心\社会与法',
'港澳台新闻','E:\dev\git\dev_code\python\Projects\history_rss\data\新闻中心\港澳台新闻'
]

def test (d):
    total = 0
    right = 0
    for i in range(0,len(d),2):
        group_name = d[i].decode('utf8')
        dir_name = d[i+1].decode('utf8')
        for root,dirs,files in os.walk (dir_name):
            print root
            for filename in files:
                full_filename = os.path.join (root,filename)
                articles = find_popular_words.read_json (full_filename,True).split('!@#$%%$#@!')
                for article in articles[:-1]:
                    label = tc.get_category_text (article)[0].decode('gbk')
                    if label ==  group_name:
                        right += 1
                    else:
                        print '-----------------------'
                        print 'should be %s but return %s ' % (group_name,label )
                        try:
                            print article
                        except:
                            pass
                        print '-----------------------'
                    total += 1
    print "total:%d , right:%d , correct rate: %.3f" % (total, right, float(right)/total) 


test (testing_dataset)

