#!/usr/bin/env python
#coding=utf-8

from script.down_files import *
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2 or not os.path.isfile(sys.argv[1]):
        print 'usage : %s template_file_path' % sys.argv[0]
        exit(1) 

    execfile (sys.argv[1])    
    for url_template, tag, rules in keys:
        start_download (make_url(url_template), rules, tag)




