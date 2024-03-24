L = int(input().strip())
S = input().strip().lower()

if len(set(S)) == 26:
    print('YES')
else:
    print('NO')