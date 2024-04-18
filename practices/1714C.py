t = int(input())

for _ in range(t):
    n = int(input())
    res = []

    for i in range(9, 0, -1):
        if i <= n:
            res.append(str(i))
            n -= i

    res.reverse()
    print("".join(res))