N, L = map(int, input().strip().split())
lamps = map(int, input().strip().split())
lamp_pos = set()

for l in lamps:
    lamp_pos.add(l)

lis = sorted(list(lamp_pos))

mx = max(float(lis[0] - 0), float(L - lis[-1]))

for i in range(1, N):
    half = (lis[i] - lis[i - 1]) / 2
    mx = max(mx, half)

print(mx)
    

