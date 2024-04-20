t = int(input())

for _ in range(t):
    s = input().strip()

    counts = {}

    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1

    ones = 0
    res = 0
    for count in counts.values():
        if count == 1:
            ones += 1
        else:
            res += 1

    print(res + ones // 2)