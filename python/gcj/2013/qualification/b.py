def read_data (filename):
    r = open(filename)
    data = r.readlines()
    r.close()
    return data

def write_result (data,filename='result2.txt'):
    w = open(filename,'w')
    for i in data:
        w.write(i)
    w.close()

def y ():
    return 'YES'

def n ():
    return 'N'


def highter_than_edge(square):
    n = len(square)
    m = len(square[0])
    for i in range(n):
        for j in range(m):
            tmp = square[i][j]
            flag = 0
            for k in range(n):
                if square[k][j] > tmp : 
                    flag += 1
                    break

            for k in range(m):
                if square[i][k] > tmp : 
                    flag += 1
                    break

            if flag == 2:
                return 'NO'

            if square[0][j] > tmp and square[i][0]> tmp :
                if square[n-1][j]>tmp and square[i][m-1]>tmp:
                    return 'NO'
    return 'YES'



def search (data):
    testcases = int(data[0])
    results = []
    k = 1
    t = 1
    while k < len(data):
        n,m = map (int,data[k].strip().split())
        k+= 1
        square = []
        for i in range(n):
            square.append (map(int,data[k].strip().split()))
            k+= 1
        results.append("Case #%d: %s\n" % (t,(highter_than_edge (square))))
        t+= 1
    write_result (results)

#search(read_data('B-small-attempt3.in'))
search(read_data('B-large.in'))

