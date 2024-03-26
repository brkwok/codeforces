T = int(input())

for _ in range(T):
    a = list(map(int, input().split()))

    res = 0

    for i in range(1, len(a)):
        if a[i] > a[0]:
            res += 1

    print(res)