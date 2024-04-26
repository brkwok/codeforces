t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    res = max(a[0], (x - a[-1]) * 2)

    for i in range(1, n):
        res = max(res, (a[i] - a[i - 1]))

    print(res)