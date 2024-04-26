t = int(input())

for _ in range(t):
    n = int(input())

    if n == 3 or n == 1:
        print(-1)
    else:
        mid = n // 2

        res = []
        for i in range(n, mid + 1 if n % 2 == 1 else mid, -1):
            res.append(i)

        for i in range(1, mid + 2 if n % 2 == 1 else mid + 1):
            res.append(i)

        print(*res)