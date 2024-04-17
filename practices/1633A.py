t = int(input())

for _ in range(t):
    n = int(input())

    if n % 7 == 0:
        print(n)
    else:
        n -= n % 10
        n += 9
        n -= n % 7
        print(n)