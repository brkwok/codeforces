t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    mx = 0
    curr = 0

    for i in a:
        if i == 0:
            curr += 1
        else:
            curr = 0
        mx = max(mx, curr)

    print(mx)