t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort(reverse=True)

    if a[0] == a[-1]:
        print('NO')
    else:
        if a[0] == a[1]:
            a[0], a[-1] = a[-1], a[0]

        print('YES')
        print(*a)