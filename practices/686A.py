n, x = map(int,input().split())

distressed = 0

for i in range(n):
    op, d = input().split()
    d = int(d)

    if op == '+':
        x += d
    else:
        if x >= d:
            x -= d
        else:
            distressed += 1

print(x, distressed)
