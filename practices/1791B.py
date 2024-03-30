t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    x = y = 0

    for d in s:
        if d == "U":
            y += 1
        elif d == "D":
            y -= 1
        elif d == "L":
            x -= 1
        else:
            x += 1

        if x == y == 1:
            print('YES')
            break
    else:
        print('NO')