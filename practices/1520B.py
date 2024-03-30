t = int(input())

for _ in range(t):
    n = int(input())
    m = n
    num_dig = 0
    base = 0
    while n > 9:
        num_dig += 1
        base = base * 10 + 1
        n //= 10

    base = base * 10 + 1
    res = (num_dig) * 9

    for i in range(1, 10):
        if base * i <= m:
            res += 1
        else:
            break
    print(res)
