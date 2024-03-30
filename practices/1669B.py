t = int(input())

from collections import Counter

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    c = Counter()

    for i in a:
        c[i] += 1

        if c[i] > 2:
            print(i)
            break
    else:
        print(-1)