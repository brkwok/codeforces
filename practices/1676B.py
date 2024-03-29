t = int(input())

for _ in range(t):
    n = int(input())
    a = sorted(list(map(int, input().split())))

    mn = a[0]
    res = 0

    for i in range(1, n):
        res += a[i] - mn

    print(res)
