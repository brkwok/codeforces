t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()
    track = set()
    score = 0

    for ch in s:
        if ch in track:
            score += 1
        else:
            track.add(ch)
            score += 2

    print(score)