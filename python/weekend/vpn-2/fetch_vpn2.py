#encoding:utf8

import os
import re


#find the fastest vpns server ip of the vpn-2 二师兄  http://www.2-vpn1.org/


class vpn_2:
  content = ''
  ip_list = []
  ping_n  = 10   #ping amount
  ping_t  = 3    #ping timeout
  ip_time = []

  def __init__ (self, filename):
    self.content = file(filename).read()

  def find_all_ip(self):
    self.ip_list = re.findall (r'''\d+\.\d+\.\d+\.\d+''', self.content)
    self.ip_list = list(set(self.ip_list))
    print 'ip list', self.ip_list

  def ping_one_ip (self, url):
    cmd = "ping -c %d -t %d %s" % (self.ping_n, self.ping_t, url)
    content = os.popen(cmd).readlines()
    line = content[-1]

    temp1 = re.search(r'''= [\d\.]+/([\d\.]+)/''', content[-1])

    temp2 = re.search(r'''([\d\.]+)% packet loss''', content[-2])

    if temp1 and temp2:
      return temp1.group(1), temp2.group(1)
    else:
      return 1000, 100

  def ping_all_ip (self):
    total = len(self.ip_list)

    for index, ip in enumerate(self.ip_list):
      print '%d/%d ping ' % (index+1, total) + str(ip) + ' ',
      temp1, temp2 = self.ping_one_ip (ip)
      print temp1, 'ms, ', temp2, '% packet loss'
      self.ip_time.append ([ip, temp1, temp2])

  def show (self):
    print '=============================='
    result = sorted (self.ip_time, key=lambda x:int(float(x[1])))
    for i in result:
      print '%20s : %6s seconds : %s packet loss' % (i[0], i[1], i[2])
    print '=============================='
    return None

  def go(self):
    self.find_all_ip()
    self.ping_all_ip()
    self.show()


if __name__ == "__main__":
  v2 = vpn_2('aa.txt')     #显示vpn 路线列表的网页源代码
  v2.go()
