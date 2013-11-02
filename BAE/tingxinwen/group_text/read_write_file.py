#coding=utf-8
import os
import codecs

def write (filename,content):
    dir_name = os.path.split(filename)[0]
    if dir_name and not os.path.isdir(dir_name):
        os.makedirs (dir_name)
    w = codecs.open(filename, "w", "utf-8")
    w.write(content)
    w.close()

def read (filename):
    r = codecs.open(filename, "r", "utf-8")
    content = r.read()
    r.close()
    return content



