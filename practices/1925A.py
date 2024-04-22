t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    chs = "abcdefghijklmnopqrstuvwxyz"

    parts = chs[:k] * n

    print(parts)