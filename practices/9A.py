Y, W = map(int, input().split())

mx = max(Y, W)
can_win = 6 - mx + 1

from math import gcd

g = gcd(can_win, 6)
print(f"{can_win//g}/{6//g}")