#coding:utf-8

from script.down_files import *

#r1 = r'''<a href='([^']+)' target='_blank'>'''
#r2 = r'''<embed src="([^"]+)"'''
#yueyu_story_keys=[['http://www.pingshu8.com/MusicList/mmc_219_341_{{1-12}}.htm','xinyou',[r1,r2]]]

r1=r'''<a href='([^']+)' title=.*?>'''
r2=r'''<embed src="([^"]+)" .*?>'''
#yueyu_story_keys=[['http://www.ysts8.com/Yshtml/Ys4477.html','hanwudadi',[r1,r2]]]
yueyu_story_keys=[['http://www.ysts8.com/Yshtml/Ys1027.html','luxiaofeng',[r1,r2]]]


for url_template, tag, rules in yueyu_story_keys:
    start_download ([url_template], rules, tag)




