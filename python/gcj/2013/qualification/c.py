import math
def read_data (filename):
    r = open(filename)
    data = r.readlines()
    r.close()
    return data

def write_result (data,filename='result3.txt'):
    w = open(filename,'w')
    for i in data:
        w.write(i)
    w.close()

def is_prime (n):
    s = str(n)
    length = len(s)
    for i in range(length/2):
        if s[i] != s[length-i-1]:
            return False
    return True

def cal_prime_square1(start,end):
    prime_num = 0
    for i in xrange(start,end+1):
        tmp = math.sqrt(i)
        if abs(int(tmp)-tmp) < 0.00001:
            if is_prime(i) and is_prime(int(tmp)):
                prime_num += 1
    return prime_num

def cal_prime_square2(start,end):
    prime_num = 0
    max_prime = int(math.sqrt(end))
    min_prime = int(math.sqrt(start))
    for i in xrange (min_prime,max_prime+1):
        if is_prime(i):
            if i*i >=start and i*i <=end:
                if is_prime(i*i):
                    prime_num += 1
    return prime_num

def cal_prime_square3 (start,end):
    n1 = len(str(start))
    n2 = len(str(end))

    prime_num = 0
    for i in range(n1,n2+1):
        if i%2==0:
            data = range(pow(10,i),pow(10,i+1))
            for j in data:
                temp = str(j) + str(j)[::-1]

        else:
            pass

    return prime_num


def search (data):
    testcases = int(data[0])
    results = []
    k = 1
    while k <= testcases:
        n,m = map (int,data[k].strip().split())
        print 'testcase',k
        results.append ('Case #%d: %d\n' % (k,cal_prime_square3(n,m)))
        k+= 1
    write_result (results)

#search(read_data('c.txt'))
#search(read_data('C-small-attempt0.in'))
search(read_data('C-large-1.in'))

