t = int(input())

for _ in range(t):
    s = int(input())

    sqrt = int(s ** 0.5)
    if sqrt * sqrt == s:
        print(sqrt)
    else:
        print(sqrt + 1)