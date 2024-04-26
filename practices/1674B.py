t = int(input())

for _ in range(t):
    berland = input().strip()
    pos1 = ord(berland[0]) - ord('a')
    pos2 = ord(berland[1]) - ord('a')

    idx = pos1 * 26 + pos2 + 1
    dups = pos1 + (pos2 >= pos1)

    print(idx - dups)

