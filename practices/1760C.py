t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))

    firstMx, secondMx = 0, 0
    for num in a:
        if num >= firstMx:
            secondMx = firstMx
            firstMx = num
        elif num > secondMx:
            secondMx = num

    res = []

    for num in a:
        if num == firstMx:
            res.append(firstMx - secondMx)
        else:
            res.append(num - firstMx)

    print(*res)
        