t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    res = 0
    for i in range(n-1):
        n1, n2 = a[i], a[i+1]
        n1, n2 = min(n1, n2), max(n1, n2)
        count = 0
        while n2 > n1 * 2:
            n1 *= 2
            count += 1
        
        res += count

    print(res)