import sys

s = raw_input()
s = s.split()
n = int(s[0])
k = int(s[1])

a = list(raw_input()+'0')
b = list(raw_input()+'0')

result = ''
for i in xrange(k):
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
        yy = 0
        yyy= 0
        for x in xrange(x1):
            yy = yy + int(a[x]) + int(b[x])
            yyy = yy % 2
            yy = yy / 2
        if x1==n:
            result += str(yy)
        else:
            result += str(yyy)

print result
