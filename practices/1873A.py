t = int(input())

for _ in range(t):
    a,b,c = list(input().strip())

    if a == 'a' or b == 'b' or c=='c':
        print('YES')
    else:
        print('NO')