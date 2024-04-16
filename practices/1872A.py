from math import ceil

t = int(input())


for _ in range(t):
    a, b, c = map(int, input().split())

    diff = abs(a - b)
    half = float(diff) / 2

    print(ceil(half / c))
