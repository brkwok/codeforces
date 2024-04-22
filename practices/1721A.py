t = int(input())

for _ in range(t):
    r1 = input().strip()
    r2 = input().strip()

    colors = set(list(r1))
    for c in r2:
        colors.add(c)

    numColors = len(colors)

    print(numColors - 1)