
import random
import time

# 在一个字符串当中，计算不同单词出现的次数

def make_case (n):
    library = ['aa','bb','cc','ee','dd','ff','gg','hello','google','world','ibm','facebook','sex','girl','program']
    #library = ['aa','bb','cc']
    result = []
    word_len = len(library)-1
    for i in range(n):
        result.append(library[random.randint(0,word_len)])

    return result

def wc1(ss):
  result = {}
  for i in ss:
    try:
      result[i] += 1
    except:
      result[i] = 1
  
  #for i in result:
    #print i,result[i]
    

def wc2(ss):
    ss.sort()
    num  = 1
    prev = 0
    for i in range(1,len(ss)):
        if ss[prev] == ss[i]:
            num += 1
        else:
           # print ss[prev],num
            num = 1
            prev = i
    #print ss[prev],num
    
def wc3(ss):
    temp = set(ss)
    for i in temp:
        #print i,ss.count(i)
        tem = ss.count(i)


def write_line():
    print '-----------------------------------'

def test():
    temp = make_case(1000000)

    t1 = time.time()
    wc1(temp)
    print time.time()-t1

    write_line()

    t2 = time.time()
    wc2(temp)
    print time.time()-t2

    write_line()

    t3 = time.time()
    wc3(temp)
    print time.time()-t3


if __name__ == "__main__":
    test()
