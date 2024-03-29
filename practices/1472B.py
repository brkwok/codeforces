from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    a = Counter(map(int, input().split()))

    if a[1] % 2 == 0 and a[2] % 2 == 0:
        print('YES')
    else:
        if a[1] % 2 == 1 and a[2] % 2 == 0:
            print('NO')
        elif a[1] % 2 == 0 and a[2] % 2 == 1:
            if a[1] == 0:
                print('NO')
            else:
                print('YES')
        else:
            print('NO')
