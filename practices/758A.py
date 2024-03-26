N = int(input())
a = list(map(int, input().split()))

mx = max(a)
res = 0
for n in a:
    if n < mx:
        res += mx - n

print(res)