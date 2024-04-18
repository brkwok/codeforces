t = int(input())

for _ in range(t):
    n,m,x = map(int,input().split())

    col = (x-1)//n + 1
    row = (x-1)%n

    print((row)*m + col)

