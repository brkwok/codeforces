t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    res = []

    for num in a:
        if num % 2 == 0:
            res.append(num)
    
    for num in a:
        if num % 2 == 1:
            res.append(num)

    print(*res)