t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    for i in range(n):
        if a[i] == k:
            print("YES")
            break
    else:
        print("NO")
