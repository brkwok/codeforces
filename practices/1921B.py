t = int(input())

for _ in range(t):
    n = int(input())
    a = input().strip()
    b = input().strip()

    x = y = z = 0

    for i in range(n):
        if a[i] == '1':
            x += 1
        if b[i] == '1':
            y += 1
        if a[i] == '1' and b[i] == '1':
            z += 1

    if x >= y:
        print(x - z)
    else:
        print(y - z)


    