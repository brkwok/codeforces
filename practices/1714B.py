t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    r = n - 1
    seen = set()
    while r >= 0:
        num = a[r]

        if num in seen:
            print(r + 1)
            break
        
        seen.add(num)
        r -= 1
    else:
        print(0)