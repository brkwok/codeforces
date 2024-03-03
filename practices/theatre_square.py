import math

n, m, a = map(int, input().strip().split())

print(math.ceil(float(n) / a) * math.ceil(float(m) / a))