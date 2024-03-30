t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    l, r =0, n -1

    for i in range(n // 2):
        print(a[l], a[r], end=' ')
        l += 1
        r -= 1

    if n % 2 == 1:
        print(a[l])
    else:
        print()