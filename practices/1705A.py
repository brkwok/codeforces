t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()

    for i in range(n):
        if a[i] + x > a[i + n]:
            print("NO")
            break
    else:
        print("YES")