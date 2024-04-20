l = int(input())
s = input().strip()

res = []

i = 0
j = 1

while i < l:
    res.append(s[i])
    i += j
    j += 1

print(''.join(res))