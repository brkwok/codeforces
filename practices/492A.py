n = int(input())

curr = 0
nxt = 1
total = 0

while total + curr + nxt <= n:
    total += curr + nxt
    curr += nxt
    nxt += 1

print(nxt - 1)