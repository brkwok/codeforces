t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    res= 0

    for i in range(n - 1):
        res = max(res, a[i] * a[i + 1])

    print(res)