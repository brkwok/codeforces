t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    res =[]

    for i in range(0, 2*n, 2):
        res.append(s[i])

    print(''.join(res))