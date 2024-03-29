t = int(input())

for _ in range(t):
    s = input().strip()
    n = len(s)

    if n % 2:
        print('NO')
    else:
        r = n // 2

        for l in range(n // 2):
            if s[l] != s[r]:
                print('NO')
                break
            r += 1
        else:
            print('YES')