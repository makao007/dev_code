filename = 'C-large-practice.in'
r = open(filename)
cases = int(r.readline())
results = []

def add_char (result, char, n):
    if not result:
        return char
    elif char[0] == result[-1] :
        return  ' '+ char
    else:
        return  char

def cal_key_press (line):
    result = ''
    for i in line:
        if i == '\n':
            continue
        elif i == ' ':
            result += add_char(result,'0',1)
        elif i in 'abcdefghijklmno':
            tmp = chr(ord('2') + (ord(i) - ord('a'))/3)
            num = (ord(i) - ord('a')) % 3 + 1
            result += add_char(result,tmp*num,3)
        elif i in 'pqrs':
            tmp = '7' * (ord(i)-ord('p')+1)
            result += add_char(result,tmp,4)
        elif i in 'tuv':
            tmp = '8' * (ord(i)-ord('t')+1)
            result += add_char(result,tmp,3)
        elif i in 'wxyz':
            tmp = '9' * (ord(i)-ord('w')+1)
            result += add_char(result,tmp,4)
        else:
            print result
            print 'unknown'
    return result

for i in range(cases):
    line = r.readline()
    results.append (cal_key_press (line))
r.close()

def write_result(results):
    k = 1
    w = open('output.txt','w')
    for i in results:
        w.write ('Case #%d: %s\n' % (k,i))
        k += 1
    w.close()

write_result(results)

