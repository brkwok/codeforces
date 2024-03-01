N = int(input().strip())

res = 0
for _ in range(N):
    s = input().strip()

    if s.find("++") >= 0:
        res += 1
    else:
        res -= 1

print(res)