t = int(input())

for _ in range(t):
    a,b,c,n = map(int, input().split())

    if (a+b+c+n)%3 == 0 and max(a,b,c) <= (a+b+c+n)//3:
        print('YES')
    else:
        print('NO')