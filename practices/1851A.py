t = int(input())

for _ in range(t):
    n,m,k,H = map(int, input().split())
    h = list(map(int, input().split()))

    if m == 1:
        print(0)
        continue
    count = 0
    for height in h:
        heightDiff = abs(height-H)

        if heightDiff % k == 0 and (m - 1) * k >= heightDiff and heightDiff != 0:
            count += 1

    print(count)