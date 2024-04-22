t = int(input())

for _ in range(t):
    s = input().strip()
    seen = set()
    days = 1

    for ch in s:
        if ch not in seen:
            if len(seen) == 3:
                seen.clear()
                days += 1
            seen.add(ch)

    print(days)