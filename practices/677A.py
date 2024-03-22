N, H = map(int, input().strip().split())
A = map(int, input().strip().split())

w = 0

for n in A:
    if n > H:
        w += 2
    else:
        w += 1

print(w)