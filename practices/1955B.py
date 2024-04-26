t = int(input())

for _ in range(t):
    n, c, d = map(int, input().split())
    a =  sorted(list(map(int, input().split())))
    base = a[0]
    b = [base + i * d for i in range(n)]

    for i in range(n):
        for j in range(1, n):
            b.append(b[i] + j * c)

    b.sort()

    if a ==b:
        print("YES")
    else:
        print("NO")

    