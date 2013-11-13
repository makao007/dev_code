#encoding=utf8

import re
import urllib

from fetch import fetch


result = ''
for i in range(8):
    url = "http://licai.taobao.com/json/show_buyer_list.html?bid_page=%d&item_id=35979593061&seller_id=1759036930&page_size=%d"
    url = url % (i+1,100)
    content = fetch(url)

    data = re.findall (r'''<tr> <td.*?>([^<]+)<span.*?>([^<]+)</span></td> <td.*?><span>([^<]+)</span><span.*?></span></td> <td.*?>([\d\.]+).*?</td> <td.*?>([^<]+)</td> <td.*?>([^<]+)</td> </tr>''',content,re.I|re.M|re.S)
    
    print i+1, len(data),"records"
    if not data:
        break
    for i in data:
        line = ','.join(i)
        result += line + '\n'

w = open('taobao_licai_jijin.txt','w')
w.write(result)
w.close()
    


