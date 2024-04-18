t = int(input())

for _ in range(t):
    n,d = input().strip().split()
    num = input().strip()
    n = int(n)

    i = 0

    while i < n and d <= num[i]:
        i += 1
    
    RES = num[:i] + d + num[i:]

    print(RES)