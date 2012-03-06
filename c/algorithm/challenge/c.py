s = raw_input()
n = int(s.split()[0])
m = int(s.split()[1])

path = [[0]*n for i in range(n)]

for i in range(m):
    ss = raw_input()
    x1 = int(ss.split()[0])-1
    x2 = int(ss.split()[1])-1

    path[x1][x2] = 1

for i in range(n):
    for j in range(n):
        print path[i][j],
    print 


