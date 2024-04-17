from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    counts = Counter(a)

    dups = sum([v - 1 for v in counts.values()])

    if dups % 2 == 0:
        print(len(counts))
    else:
        print(len(counts) - 1)