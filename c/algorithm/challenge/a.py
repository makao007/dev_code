s = raw_input()
n = int(s.split()[0])
k = int(s.split()[1])
result = []
for i in range(n):
        result.append(int(raw_input()))
            
result.sort()
for i in range(k):
    result.pop(0)

print sum(result)
