t = int(input())

for _ in range(t):
    a = input().strip()
    b = input().strip()

    even = False

    for i, ch in enumerate(a):
        if ch == b and i % 2 == 0:
            even = True
            break

    if even:
        print('YES')
    else:
        print('NO')