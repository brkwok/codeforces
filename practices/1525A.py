t = int(input())

def gcd(n, m):
    if n == 0:
        return m
    return gcd(m % n, n)

for _ in range(t):
    n = int(input())

    if 100 % n == 0:
        print(100//n)
    else:
        g = gcd(n, 100)
        print(100//g)