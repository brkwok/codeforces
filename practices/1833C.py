t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    minOdd = float('inf')
    minEven = float('inf')

    for num in a:
        if num % 2 == 0:
            minEven = min(minEven, num)
        else:
            minOdd = min(minOdd, num)
    
    if minEven == float('inf') or minOdd == float('inf') or minEven > minOdd:
        print("YES")
    else:
        print("NO")