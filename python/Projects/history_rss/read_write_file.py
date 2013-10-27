#coding=utf-8

import codecs

def write (filename,content):
    w = codecs.open(filename, "w", "utf-8")
    w.write(content)
    w.close()

def read (filename):
    r = codecs.open(filename, "r", "utf-8")
    content = r.read()
    r.close()
    return content



