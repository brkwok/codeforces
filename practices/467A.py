N = int(input().strip())

res = 0

for _ in range(N):
    P, Q = map(int, input().strip().split())
    if Q - P >= 2:
        res += 1

print(res)