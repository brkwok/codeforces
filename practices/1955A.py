t = int(input())

for _ in range(t):
    n,a,b = map(int,input().split())

    res = n // 2 * b + n % 2 * a
    print(res)