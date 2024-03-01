N = 5

for i in range(N):
    r = input().strip()
    one_loc = r.find("1")

    if one_loc>= 0:
        break

r, c = i, one_loc // 2

print(abs(r - 2) + abs(c - 2))