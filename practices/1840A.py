t = int(input())

for _ in range(t):
    l = int(input())
    s = input().strip()

    decoded = []
    prev = None

    for ch in s:
        if prev is None:
            decoded.append(ch)
            prev = ch
        else:
            if ch == prev:
                prev = None

    print(''.join(decoded))
