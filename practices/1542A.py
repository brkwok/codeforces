t = int(input())

for _ in range(t):
    n = int(input())
    a = map(int, input().split())

    parity = 0

    for i in a:
        if i % 2 == 0:
            parity += 1
        else:
            parity -= 1

    if parity == 0:
        print('Yes')
    else:
        print('No')