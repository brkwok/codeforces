t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())), reverse=True)

    for i in range(k):
        if a[i] < b[i]:
            a[i] = b[i]
        else:
            break
        
    
    print(sum(a))