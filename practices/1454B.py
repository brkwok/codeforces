t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    d = {}

    for i, n in enumerate(a):
        if n in d:
            d[n].append(i)
        else:
            d[n] = [i]

    uniqs = []

    for k, v in d.items():
        if len(v) == 1:
            uniqs.append(k)

    if len(uniqs) == 0:
        print(-1)
    else:
        print(d[min(uniqs)][0] + 1)
