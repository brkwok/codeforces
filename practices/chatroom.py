s = input().strip()
N = len(s)
p = 0

while p < N and s[p] != 'h':
    p += 1

while p < N and s[p] != 'e':
    p += 1

while p < N and s[p] != 'l':
    p += 1

p += 1

while p < N and s[p] != 'l':
    p += 1

while p < N and s[p] != 'o':
    p += 1

if p < N:
    print("YES")
else:
    print("NO")
