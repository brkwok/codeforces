t = int(input())

for _ in range(t):
    x, y, z = map(int, input().split())
    counts = {}
    mx = max(x, y, z)
    counts[x] = counts.get(x, 0) + 1
    counts[y] = counts.get(y, 0) + 1
    counts[z] = counts.get(z, 0) + 1

    if len(counts) == 3 or counts[mx] < 2:
        print("NO")
    else:
        print("YES")
        if x == y == z:
            print(x, y, z)
        else:
            print(mx, min(x, y, z), min(x, y, z))
