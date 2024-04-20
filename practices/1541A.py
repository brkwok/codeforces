t = int(input())

for _ in range(t):
    n = int(input())

    res = []

    for i in range(1, n, 2):
        res.append(i + 1)
        res.append(i)

    if n % 2:
        res.append(n)
        res[-1], res[-2] = res[-2], res[-1]

    print(*res)