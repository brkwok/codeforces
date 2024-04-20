t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    counts = [0] * 27

    for c in s:
        counts[ord(c) - ord('A') + 1] += 1

    solved = 0

    for i in range(1, 27):
        if counts[i] >= i:
            solved += 1

    print(solved)