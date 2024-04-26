from math import sqrt

t = int(input())

for _ in range(t):
    n = int(input())
    if n == 1:
        print(1, 1)
        continue
    sq = int(sqrt(n - 1)) + 1

    mid = ((sq - 1) ** 2 + 1 + (sq ** 2)) // 2

    if n == mid:
        print(sq, sq)
    elif n < mid:
        print(sq - (mid - n), sq)
    else:
        print(sq, sq - (n - mid))
    