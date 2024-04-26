t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    prev = None
    streak = 0
    maxStreak = 0
    for i in range(n):
        if not prev:
            prev = a[i]
            streak += 1
            continue

        if a[i] == prev:
            streak += 1
        else:
            prev = a[i]
            maxStreak = max(maxStreak, streak)
            streak = 1

    maxStreak = max(maxStreak, streak)
    
    print(maxStreak)