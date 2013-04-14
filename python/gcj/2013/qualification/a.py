def read_data (filename):
    r = open(filename)
    data = r.readlines()
    r.close()
    return data

def write_result (data,filename='result.txt'):
    w = open(filename,'w')
    for i in data:
        w.write(i)
    w.close()

def x_win ():
    return 'X won'

def o_win ():
    return 'O won'

def not_win(data):
    for i in data:
        if '.' in i:
            return 'Game has not completed'
    return 'Draw'

def who_win (square):
    options = []
    for i in range(len(square)):
        options.append (square[i])

    for i in range(len(square)):
        tmp= ''
        for j in range(len(square)):
            tmp += square[j][i]
        options.append(tmp)
    
    
    tmp = ''
    for i in range(len(square)):
        tmp += square[i][i]
    options.append(tmp)

    tmp = ''
    for i in range(len(square)):
        tmp  += square[i][len(square)-i-1]
    options.append(tmp)
        
    for tmp in options:
        if tmp == 'XXXX' or tmp == 'XXXT':
            return x_win()
        if tmp == 'OOOO' or tmp == 'OOOT':
            return o_win()
    return not_win(square)



def search (data):
    testcases = int(data[0])
    results = []
    for i in range(testcases):
        square = []
        for j in range(4):
            square.append (data[i*5+j+1].strip())

        result = who_win (square)
        results.append ('Case #%d: %s\n' % (i+1,result)) 
    write_result(results)
        

search(read_data('a.txt'))
