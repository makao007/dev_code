s = raw_input()
n = int(s.split()[0])
k = int(s.split()[1])
total = 0

i = 0
while i<n:
    result = []
    j = 0
    while j<=k and i<n:
        result.append(int(raw_input()))
        i += 1
        j += 1
    result.sort()
    if len(result) == (k+1):
        result.pop(0)
    total += sum(result)

print total
