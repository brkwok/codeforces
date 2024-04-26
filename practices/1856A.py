t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    mx = a[0]
    bp = None
    for i in range(n - 1, 0, -1):
        if a[i] > mx:
            mx = a[i]
        
        if a[i] < a[i - 1]:
            bp = i
            break
    else:
        print(0)
        continue

    mx = max(a[:bp])
    print(mx)
