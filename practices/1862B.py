t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    res = []

    for num in a:
        if not res or res[-1] <= num:
            res.append(num)
        else:
            res.append(num)
            res.append(num)
    
    print(len(res))
    print(*res)
