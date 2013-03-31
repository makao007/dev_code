filename = 'B-large-practice.in'

r = open(filename)
cases = int(r.readline())

def write_result (results):
    w = open('q2_result.txt','w')
    k = 1
    for result in results:
        w.write ('Case #%d: %s\n' % (k,result))
        k +=1
    w.close()

results = []
for i in range(cases):
    line = r.readline()
    words = line.split()
    result = ' '.join(words[::-1])
    results.append(result)
r.close()

write_result(results)
    

