#coding:utf-8
#/usr/bin/env python

from script.down_files import *

r1 = r'''<a href='([^']+)' target='_blank'>'''
r2 = r'''<embed src="([^"]+)"'''
yueyu_story_keys=[['http://www.pingshu8.com/MusicList/mmc_219_341_{{1-12}}.htm','xinyou',[r1,r2]]]


for url_template, tag, rules in yueyu_story_keys:
    start_download (make_url(url_template), rules, tag)




