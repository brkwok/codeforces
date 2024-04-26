t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    conv = []

    for i in range(n):
        conv.append(input().strip())


    res = 0

    for i in range(n):
        if conv[i][m - 1] == 'R':
            res += 1
    
    for j in range(m):
        if conv[n - 1][j] == 'D':
            res += 1

    print(res)