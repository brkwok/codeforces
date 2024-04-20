t = int(input())

for _ in range(t):
    n,m,k = map(int, input().split())

    res = n - 1 + n * (m - 1)

    if res == k:
        print("YES")
    else:
        print("NO")