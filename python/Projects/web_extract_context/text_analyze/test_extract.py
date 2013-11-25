#encoding=utf-8
#!/usr/bin/env python 

from extract import *

def find_content_position (content):
    return method_1 (content)

def find_content_position_known (content,start_partern, end_partern):
    if not content:
        return None,None,None,None
    content = remove_empty_line(remove_js_css(content))
    
    start_index = content.index(start_partern)
    end_index   = content.index(end_partern)
    start_line  = content[:start_index].count('\n')
    end_line    = content[:end_index  ].count('\n')

    return start_line, end_line, start_index, end_index
