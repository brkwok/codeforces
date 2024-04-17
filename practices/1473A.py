t = int(input())

for _ in range(t):
    n,d = map(int, input().split())
    a = list(map(int, input().split()))

    if max(a) <= d:
        print("YES")
    else:
        a.sort()
        if a[0] + a[1] <= d:
            print("YES")
        else:
            print("NO")