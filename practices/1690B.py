t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a_max = max(a)
    b_max = 0
    for i in range(n):
        if b[i] != 0:
            a_max = min(a_max, a[i] - b[i])
        b_max = max(b_max, a[i] - b[i])

    if a_max == b_max:
        print("YES")
    else:
        print("NO")
