t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    res = []
    seen = set()
    for i in a:
        if i not in seen:
            res.append(i)
            seen.add(i)

    print(*res)