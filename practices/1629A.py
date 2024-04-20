t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for ai, bi in sorted(zip(a, b), key = lambda x: x[0]):
        if ai <= k:
            k += bi
        else:
            break

    print(k)