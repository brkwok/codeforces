t = int(input())
from math import ceil
for _ in range(t):
    n, x = map(int, input().strip().split())

    if n < 3:
        print(1)
    else:
        print(2 + (n - 3) // x)