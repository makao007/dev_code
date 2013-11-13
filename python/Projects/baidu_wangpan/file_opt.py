#encoding=utf-8

import os
import time
import urllib

from fetch import fetch

def timestamp ():
    return str(time.time()).replace('.','')

def show_files (content):
    print content
    obj = eval(content)
    filenames = [(i.get('server_filename'),i.get('isdir')) for i in obj.get('list')]
    for i,j in filenames:
        line = '%s  %s' % (i, 'd' if j else 'f')
        print line

def ls (dir_name,cookie):
    dir_name = urllib.quote(dir_name,safe='')
    url = 'http://pan.baidu.com/api/list?channel=chunlei&clienttype=0&web=1&num=100&t=%s&page=1&dir=%s&t=0.66061&order=time&desc=1&_=%s' % (timestamp(),dir_name,timestamp())

    content = fetch(url,None,cookie)
    show_files (content)


def show_help ():
    print '------------------------'
    print ' ls [dir]       -- list the files'
    print ' cd [dir]       -- change the current directory'
    print ' tree           -- list all the files with sub directory from current directory'
    print ' help           -- show this help menu'
    print ' exit           -- exit'
    print '------------------------'

def login_baidu ():
    url = 'https://passport.baidu.com/v2/api/?login'
    header = {'staticpage':'http://pan.baidu.com/res/static/thirdparty/pass_v3_jump.html',
                'charset':'utf-8',
                'token':'cb43da0cb6c17aa9f58a44369d624d67',
                'tpl':'netdisk',
                'apiver':'v3',
                'tt':timestamp(),
                'codestring':'',
                'isPhone':'false',
                'safeflg':'0',
                'u':'http://pan.baidu.com/',
                'quick_user':'0',
                'logintype':'basicLogin',
                'username':'makao007@gmail.com',
                'password':'B55665566',
                'verifycode':'',
                'mem_pass':'on',
                'ppui_logintime':'10423',
                'callback':'parent.bd__pcbs__dikal3'
            }


    print url
    return fetch(url,header,None,True)

def main () :
    content,cookie = login_baidu()
    print content
    print cookie
    curr_path = '/'
    show_help ()


    while 0:
        print '>>>',
        line = raw_input ().strip().split()
        line[0] = line[0].lower()

        input_error = False
        if len(line)==1:
            if line[0] not in ['cd','ls','exit','tree']:
                input_error = True
        elif len(line)==2:
            if line[0] != 'ls' and line[0].lower() != 'cd':
                input_error = True
        else:
            input_error = True
        
        if input_error :
            print 'Input Error'
            show_help()
        else:
            tmp_path = curr_path
            if len(line)==2 :
                if line[1].startswith('/'):
                    tmp_path = line[1]
                else:
                    tmp_path = os.path.join(curr_path,line[1])

            # parse the command , call corespond function
            if line[0] == 'help':
                show_help()
            elif line[0] == 'cd':
                curr_path = tmp_path
            elif line[0] == 'ls':
                ls (tmp_path,cookie)
            elif line[0] == 'tree':
                tree (curr_path)
            elif line[0] == 'exit' or line[0] == 'quit':
                break
            else:
                print 'Input Error'
                show_help()



if __name__ == "__main__":
    main()
    

