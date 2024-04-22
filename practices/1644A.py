t = int(input())

for _ in range(t):
    s = input().strip()

    keys = set()

    for ch in s:
        if ch.lower() == ch:
            keys.add(ch)
        else:
            if ch.lower() not in keys:
                print('NO')
                break
    else:
        print("YES")