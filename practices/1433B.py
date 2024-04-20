t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    l, r = 0, n - 1

    while l < r and a[l] == 0:
        l += 1
    while r > l and a[r] == 0:
        r -= 1

    if l == r:
        print(0)
    else:
        zeroCount = 0

        for i in range(l, r + 1):
            if a[i] == 0:
                zeroCount += 1
        
        print(zeroCount)

    