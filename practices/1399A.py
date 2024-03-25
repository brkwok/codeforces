T = int(input())

for _ in range(T):
    n = int(input())
    a = sorted(list(map(int, input().split())))

    removed = 0
    for i in range(1, n):
        if a[i] - a[i-1] > 1:
            break
        removed += 1
    
    if removed == n - 1:
        print('YES')
    else:
        print('NO')