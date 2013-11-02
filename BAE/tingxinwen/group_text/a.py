#encoding=utf-8

from TextClassification import TextClassification

#the first testcase, load the default infomation file
tc = TextClassification()
tc.load_info_file ('info.dat')        #the info.dat file is make by myself, this file can by genereate through "tc.train_dataset(filename)", you can refer below
print tc.get_category_text ('stock etf ipo')[0]        #test, get text category 
#财经新闻

print tc.get_category_text ('地产，一平米上万块听')[0]
#房产新闻

#------------------------------------------
tc = TextClassification()
tc.train_dataset('a.txt')        #create a new infomation file  
print tc.get_category_text ('stock etf ipo')[0]
print tc.get_category_text ('地产，一平米上万块听')[0]
tc.save_info_file ('two.dat')    #save the infomatin file   


#------------------------------------------
tc = TextClassification()
tc.load_info_file ('two.dat')        #the info.dat file is make by myself
print tc.get_category_text ('stock etf ipo')[0]
print tc.get_category_text ('地产，一平米上万块听')[0]
tc.save_top_words('key_words_folder')   # you can see it will generate some txt files in inside the key_words_folder 
