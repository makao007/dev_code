#encoding=utf-8

import os

from extract import *


def list_all_file (dir_name):
    result = []
    for root,dir_path,filenames in os.walk (dir_name):
        for filename in filenames:
            result.append (os.path.join(root,filename))
    return result

def filter_files (filenames,post_fix=[]):
    return filter (lambda x:os.path.splitext(x)[1].lower() in post_fix, filenames)

def write_file (filename,content):
    dir_name = os.path.split(filename)[0]
    if dir_name and not os.path.isdir(dir_name):
        os.makedirs(dir_name)
    w = open(filename,'w')
    w.write(content)
    w.close()



def make_feature (dir_name):
    """ extract the feature for cnbeta test data set"""
    filenames = filter_files (list_all_file (dir_name),['.html','.htm'])
    result = []
    index = 1
    total_score = 0.0
    for filename in filenames:
        content = file(filename).read()
        content = remove_empty_line(remove_js_css(content))
        total_lines = float(content.count('\n'))


        start,end,start_index,end_index  = find_content_position_known (content, \
                '<div class="introduction">','                    <div class="clear"></div>')
        msg  = ("%-8d %-8d %-8d %-8d %s" % (start,end, start_index, end_index, filename))
        write_file ('generate_known/' + os.path.split(filename)[1], '\n'.join(content.split('\n')[start:end]))


        start_2,end_2,start_index,end_index  = find_content_position (content)
        msg2 = ("%-8d %-8d %-8d %-8d %s" % (start_2,end_2, start_index, end_index, filename))
        write_file ('generate_unknown/' + os.path.split(filename)[1], '\n'.join(content.split('\n')[start_2:end_2]))

        score = 0
        if start_2 < start:
            score += (start - start_2 ) * 0.5
        else:
            score += (start_2 - start ) * 2

        if end_2 > end :
            score += (end_2 - end) * 0.5
        else:
            score += (end - end_2) * 2
        score /= total_lines
        total_score += score



        if score > 0.1 :
            print filename

        result.append (msg)
        result.append (msg2)
        result.append ('-----   %.3f' % score)
        print index
        if index == 1000:
            break
        index += 1

    result.append ("total mean score is %.3f" % (total_score/len(filenames)))
    write_file ('result.txt','\n'.join(result))


if __name__ == "__main__":
    make_feature("d:/Data/cnbeta/")
    #make_feature("d:/Data/small_cnbeta")
    #make_feature("d:/Data/middle_cnbeta")

