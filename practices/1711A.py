t = int(input())

for _ in range(t):
    n = int(input())

    res = list(range(1, n + 1))
    for i in range(0, n - 1, 2):
        res[i], res[i + 1] = res[i + 1], res[i]
    
    if n % 2 == 1 and n > 2:
        res[-1], res[-2] = res[-2], res[-1]

    print(*res)
