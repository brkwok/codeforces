T = int(input())

for _ in range(T):
    a, b = map(int, input().split())

    need = abs(a - b)
    res = need // 10

    if need % 10:
        res += 1

    print(res)