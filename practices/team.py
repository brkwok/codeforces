from functools import reduce

T = int(input().strip())

res = 0
for _ in range(T):
    val = reduce(lambda x, y: x + y, map(int, input().strip().split()), 0)
    
    if val >= 2:
        res += 1

print(res)

        