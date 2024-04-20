t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    diffs = []

    for i in range(n - 1):
        diff = a[i + 1] - a[i]

        if diff < 0:
            print(0)
            break

        diffs.append(diff)
    else:
        print(min(diffs) // 2 + 1)