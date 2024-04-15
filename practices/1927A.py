t = int(input().strip())

for _ in range(t):
    n = int(input())
    s = input().strip()

    first, last = -1, -1

    for i, ch in enumerate(s):
        if ch == "B":
            if first == -1:
                first = i

            last = i

    print(0 if first == -1 else (last - first + 1))