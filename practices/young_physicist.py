N = int(input().strip())

s = [0] * 3

for _ in range(N):
    v = map(int,input().strip().split())
    for i,v in enumerate(v):
        s[i] += v
    
for n in s:
    if n != 0:
        print("NO")
        break
else:
    print("YES")