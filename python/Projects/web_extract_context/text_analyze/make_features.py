#encoding=utf-8

import os

from extract import remove_js_css,find_content_position_known 


def list_all_file (dir_name):
    result = []
    for root,dir_path,filenames in os.walk (dir_name):
        for filename in filenames:
            result.append (os.path.join(root,filename))
    return result

def filter_files (filenames,post_fix=[]):
    return filter (lambda x:os.path.splitext(x)[1].lower() in post_fix, filenames)

def write_file (filename,content):
    w = open(filename,'w')
    w.write(content)
    w.close()



def make_feature (dir_name):
    """ extract the feature for cnbeta test data set"""
    filenames = filter_files (list_all_file (dir_name),['.html','.htm'])
    result = []
    for filename in filenames:
        content = remove_js_css(file(filename).read())
        start,end,start_index,end_index  = find_content_position_known (content,'<div class="introduction">','                    <div class="clear"></div>')
        result.append ("%-8d %-8d %-8d %-8d %s" % (start,end, start_index, end_index, filename))

        #write_file ('content_' + os.path.split(filename)[1], '\n'.join(content.split('\n')[start:end]))
    write_file ('result.txt','\n'.join(result))


if __name__ == "__main__":
    #make_feature("d:/Data/cnbeta/")
    make_feature(".")


