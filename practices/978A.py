n = int(input())
a = list(map(int, input().split()))

seen = set()
res = []
for i in range(n - 1, -1 , -1):
    if a[i] not in seen:
        seen.add(a[i])
        res.append(a[i])

res.reverse()

print(len(res))
print(*res)