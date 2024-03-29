t = int(input())

for _ in range(t):
    a,b,c,d = map(int, input().split())

    if (a > c and a > d and b > c and b > d) or (c > a and c > b and d > a and d > b):
        print('NO')
    else:
        print('YES')