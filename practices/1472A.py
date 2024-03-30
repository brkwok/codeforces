t = int(input())

for _ in range(t):
    w, h, n = map(int, input().split())

    res = 1

    while w % 2 == 0:
        w //= 2
        res *= 2

    while h % 2 == 0:
        h //= 2
        res *= 2

    if res >= n:
        print("YES")
    else:
        print('NO')
