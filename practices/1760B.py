t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    res = 0

    for i in range(n):
        res = max(res, ord(s[i]) - 97 + 1)

    print(res)