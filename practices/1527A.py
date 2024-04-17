t = int(input())

for _ in range(t):
    n = int(input())

    n = n | (n >> 1)
    n = n | (n >> 2)
    n = n | (n >> 4)
    n = n | (n >> 8)
    n = n | (n >> 16)
    n = n | (n >> 32)
    print(n - (n >> 1) - 1)