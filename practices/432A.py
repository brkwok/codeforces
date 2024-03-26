N, K = map(int, input().split())

P = list(map(int, input().split()))

need = 5 - K
count = 0

for n in P:
    if n <= need:
        count += 1

print(count // 3)