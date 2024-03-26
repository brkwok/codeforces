T = int(input())

for _ in range(T):
    s = input().strip()
    n = len(s)

    res = [s[0]]

    for i in range(1, n - 1, 2):
        res.append(s[i])
    res.append(s[-1])

    print(''.join(res))