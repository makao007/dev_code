filename='A-large-practice.in'
r = open(filename)
cases = r.readline()
def cal_max (credit,data):
    print data
    maxA=0
    maxB=0
    maxResult = credit
    for i in range(len(data)-1):
        for j in range(i+1,len(data)):
            tmp = credit - data[i] - data[j] 
            if tmp >= 0 and tmp< maxResult:
                maxA=i
                maxB=j
                maxResult = tmp
    return (maxA,maxB)



def writeResult(result):
    w = open('result.txt','w')
    for i,j in result:
        w.write ('Case #%d: %d %d\n' % (i+1,j[0]+1,j[1]+1))
    w.close()

results=[]
for i in range(int(cases)):
    credit = int(r.readline())
    num = int(r.readline())
    data = map(int,r.readline().split())
    result = cal_max (credit,data)
    results.append ((i,result))
r.close()

writeResult(results)






