n = int(input())
a = list(map(int, input().split()))

mx = mn = a[0]
res = 0
for i in range(1, n):
    if a[i] > mx:
        mx = a[i]
        res += 1
    elif a[i] < mn:
        mn = a[i]
        res += 1

print(res)