t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = list(map(int, input().split()))

    res = [s[0] - a[0]]

    for i in range(1, n):
        res.append(s[i] - max(s[i - 1], a[i]))
    print(*res)