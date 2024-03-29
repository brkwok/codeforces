t = int(input())

for _ in range(t):
    n = int(input())

    if n % 2 == 1:
        print('NO')
    else:
        s1 = 'AA'
        s2 = 'BB'
        res =[]

        for i in range(n//2):
            if i % 2:
                res.append(s1)
            else:
                res.append(s2)

        print('YES')
        print(''.join(res))
