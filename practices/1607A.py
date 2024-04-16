t = int(input())

for _ in range(t):
    keys = {ch: i for i, ch in enumerate(input().strip())}
    s = input().strip()

    res = 0

    for i in range(1, len(s)):
        res += abs(keys[s[i]] - keys[s[i - 1]])

    print(res)
