t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    evenCount = 0
    totalEven = 0
    evenCountOdd = 0
    totalEvenOdd = 0

    for i in range(0, n, 2):
        num = a[i]
        if num % 2 == 0:
            evenCount += 1
        totalEven += 1

    for i in range(1, n, 2):
        num = a[i]
        if num % 2 == 0:
            evenCountOdd += 1
        totalEvenOdd += 1

    if (evenCount == totalEven or evenCount == 0) and (evenCountOdd == totalEvenOdd or evenCountOdd == 0):
        print('YES')
    else:
        print('NO')
    