t = int(input())

for _ in range(t):
    n = int(input())

    if n == 1:
        print(0)
        continue
    power = 1

    while 10 ** power <= n:
        power += 1

    print(n - 10 ** (power - 1))
