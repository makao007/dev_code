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

def is_con (a):
    for i in a:
        if i in 'aeiou':
            return False
    return True

def find_result(a,b):
    print
    b = int(b)
    length = len(a)
    sum = 0
    if length < b:
        return sum 
    i = 0
    while i <= length-b:
        tmp = a[i:i+b]
        if not is_con(tmp):
            i+= 1
            continue
        sum += 1

        
        temp1 = 0
        j = i-1
        while j>=0:
            if is_con(a[j:j+b]):
                break
            temp1 += 1
            j -= 1
        
        temp2 = 0
        j = i+1
        while j+b <= length:
            #if is_con(a[j:j+b]):
            #   break
            temp2 += temp1
            j += 1
            temp0 += 1

        print sum,temp0,temp1,temp2
        sum += temp0 + temp1 + temp2
        i+= 1
    return sum


    

def search (data):
    testcases = int(data[0])
    results = []
    for i in range(testcases):
        str1,str2 = data[i+1].split()
        result = find_result(str1,str2)
        results.append ('Case #%d: %d\n' % (i+1,result)) 
    write_result(results)
        

#search(read_data('A-small-attempt0.in'))
search(read_data('a.txt'))
