t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    sm = sum(a)

    if sm % n != 0:
        print(-1)
    else:
        avg = sm // n
        res = sum([1 for i in a if i > avg])

        print(res)