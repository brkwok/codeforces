t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    res = []
    for ch in s:
        if ch == 'U':
            res.append('D')
        elif ch == 'D':
            res.append('U')
        else:
            res.append(ch)

    print(''.join(res))