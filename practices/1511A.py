t = int(input())

for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))

    res = 0

    for voter in r:
        if voter == 1 or voter == 3:
            res += 1

    print(res)