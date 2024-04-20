t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    firstMx, secondMx = 0, 0

    for num in a:
        if num > firstMx:
            secondMx = firstMx
            firstMx = num
        elif num > secondMx:
            secondMx = num

    if firstMx - 1 > secondMx:
        print("NO")
    else:
        print("YES")