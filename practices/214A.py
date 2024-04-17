from math import sqrt

n, m = map(int, input().split())

count = 0

s = n + m

for i in range(int(sqrt(s)) + 1):
    for j in range(int(sqrt(s)) + 1):
        if i * i + j == n and i + j * j == m:
            count += 1

print(count)