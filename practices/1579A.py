t = int(input())

from collections import Counter

for _ in range(t):
    s = input().strip()
    c = Counter(s)

    if c["A"] + c["C"] == c["B"]:
        print("YES")
    else:
        print("NO")