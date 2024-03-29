t = int(input())

name = "Timur"
for _ in range(t):
    n = int(input())
    s = input().strip()

    if n != 5:
        print('NO')
    else:
        count = [0] * 5
        for ch in s:
            if ch == 'T':
                count[0] += 1
            elif ch == 'i':
                count[1] += 1
            elif ch == 'm':
                count[2] += 1
            elif ch == 'u':
                count[3] += 1
            elif ch == 'r':
                count[4] += 1
            else:
                print('NO')
                break
        else:
            if all([count[i] == 1 for i in range(5)]):
                print('YES')
            else:
                print('NO')