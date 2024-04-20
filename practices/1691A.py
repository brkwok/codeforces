t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    evenCount = 0
    oddCount = 0

    for num in a:
        if num % 2 == 0:
            evenCount += 1
        else:
            oddCount += 1
    
    print(min(evenCount,oddCount))