t = int(input())

for _ in range(t):
    n = int(input())
    a = [i for i in range(1, n + 1)]


    for i in range(0, n - 1, 2):
        a[i], a[i + 1] = a[i + 1], a[i]

    if n % 2:
        a[0] ,a[-1] = a[-1], a[0]

    print(*a)


        
