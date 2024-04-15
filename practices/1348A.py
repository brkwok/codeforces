t = int(input())

for _ in range(t):
    n = int(input())

    n1 = n2 = 0

    for i in range(1, n // 2):
        n1 |= (1 << i)

    n1 |= (1 << n)
    for i in range(n//2, n):
        n2 |= (1 << i)

    print(n1 - n2)