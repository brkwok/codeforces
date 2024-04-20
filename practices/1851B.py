t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)

    for i in range(n):
        if a[i] & 1 != b[i] & 1:
            print("NO")
            break
    else:
        print("YES")