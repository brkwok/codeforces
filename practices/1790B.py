t = int(input())

for _ in range(t):
    n,s,r = map(int, input().split())

    missing_die = s - r
    res = [missing_die]

    avg = r // (n - 1)
    rm = r % (n - 1)
    res.extend([avg + 1] * rm )
    res.extend([avg] * (n - 1 - rm))

    print(*res)