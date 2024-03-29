t = int(input())

for _ in range(t):
    n = int(input())
    a = sorted(list(map(int, input().split())))

    mn = 10**9

    for i in range(1, n):
        mn = min(mn, a[i] - a[i-1])
    
    print(mn)