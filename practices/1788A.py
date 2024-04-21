t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    twoCount = a.count(2)

    if twoCount == 0:
        print(1)
    elif twoCount % 2 == 1:
        print(-1)
    else:
        half = twoCount // 2
        i = 0

        while i < n and twoCount > half:
            if a[i] == 2:
                twoCount -= 1
            i += 1
        print(i)