t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    odd = 0
    even = 0

    for i in a:
        if i % 2 == 0:
            even += i
        else:
            odd += i

    if even > odd:
        print('YES')
    else:
        print('NO')