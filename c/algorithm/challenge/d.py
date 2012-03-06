import sys

s = raw_input()
s = s.split()
n = int(s[0])
k = int(s[1])

a = list(raw_input())
b = list(raw_input())

for i in range(k):
    ss = raw_input()
    ss = ss.split()
    f = ss[0]
    x1 = int(ss[1])

    if f=='set_a' or f=='set_b':
        x2 = ss[2]

        if f == 'set_a':
            a[x1] = x2
        else:
            b[x1] = x2

    elif f == 'get_c':
        aa = ''.join(a)[::-1]
        bb = ''.join(b)[::-1]
        temp = bin(int(aa,2)+int(bb,2))[2:][::-1]
        if len(temp)<=x1:
            sys.stdout.write('0')
        else:
            sys.stdout.write(temp[x1])


