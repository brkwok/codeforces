N, M = map(int, input().strip().split())

full = "#" * M
d = 0
a = "#" + "." * (M - 1)
b = "." * (M - 1) + "#"

res = []

for i in range(N):
    if i % 2 == 0:
        res.append(full)
    else:
        if d % 2 == 0:
            res.append(b)
        else:
            res.append(a)
        d = (d + 1) % 2

print("\n".join(res))