t = int(input())

for _ in range(t):
    n = int(input())

    if n % 2050 != 0:
        print(-1)
    else:
        n //= 2050
        print(sum(map(int, str(n))))