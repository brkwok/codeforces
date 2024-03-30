t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    
    zero_count = 0
    mn = 10
    prod = 1

    for i in a:
        if i == 0:
            zero_count += 1
        else:
            prod *= i
            mn = min(mn, i)

    if zero_count > 1:
        print(0)
    else:
        if zero_count == 1:
            print(prod)
        else:
            print((prod // mn) * (mn + 1))