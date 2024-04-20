t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    l, r = 0, n - 1
    sign = -1
    count = 0
    sm = sum(num if num > 0 else -num for num in a)
    while l <= r:
        while l <= r and sign * a[l] <= 0:
            l += 1
        
        while l <= r and sign * a[r] <= 0:
            r -= 1

        if l <=r :
            count += 1

        sign = -sign
    
    print(sm, count)