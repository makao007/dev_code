#coding:utf-8
from down_files import *


yueyu_story = 'http://www.ysts8.com/Ysmp3/51_{{1-3}}.html'
yueyu_param = r'''<a href=["']([^'"]+)["'] target='_blank'>([^<]+)</a>'''
yueyu_story_keys = find_match(make_url(yueyu_story), yueyu_param , True)

single_param = r'''<li class='qxx'><a href=["']([^'"]+)["'] title=["'][^'"]+["'] target='_blank'>[^<]+</a>'''
detail_param = r'''<param name="URL" value=["']([^"']+)["']>'''


#yueyu_story_keys=[['http://www.ysts8.com/Yshtml/Ys7859.html', '贼猫']]
yueyu_story_keys=[['http://www.pingshu8.com/MusicList/mmc_219_341_1.htm','西游记']]

"""
for i,j in yueyu_story_keys:
    temp = find_match([i],single_param)
    for tem in temp:
        print 'downloading ...',tem
        download_to_local (find_match([tem],detail_param),j)
    #download_to_local(find_match(find_match([i],single_param), detail_param), j)
"""

down_files.download_to_local(show_url(find_match(find_match(make_url(template_url),param1), param2)))
