t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    mx = max(a)
    mn = min(a)

    if mx == mn:
        print(-1)
    else:
        b = []
        c = []

        for num in a:
            if num == mx:
                c.append(num)
            else:
                b.append(num)

        print(len(b), len(c))
        print(*b)
        print(*c)
    
