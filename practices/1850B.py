t = int(input())

for _ in range(t):
    n = int(input())
    quality = 0
    idx = 0

    for i in range(n):
        a,b = map(int, input().split())

        if a <= 10 and b > quality:
            quality = b
            idx = i
        
    print(idx + 1)