t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    in_place = 0

    for i in range(n):
        if a[i] == i + 1:
            in_place += 1

    print(in_place // 2 + in_place % 2)