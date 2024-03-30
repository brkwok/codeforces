t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a_min = min(a)
    b_min = min(b)

    res = 0
    # 1 2 3 4 5 a_min = 1
    # 5 4 3 2 1 b_min = 1
    for i in range(n):
        min_from_both = min(a[i] - a_min, b[i] - b_min)
        res += min_from_both + (a[i] - min_from_both - a_min) + (b[i] - min_from_both - b_min)


    print(res)