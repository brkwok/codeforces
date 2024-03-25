T = int(input())

for _ in range(T):
    a = map(int, input().split())
    mx= 0
    total = 0
    for i in a:
        if i > mx:
            mx = i

        total += i
    if total - mx == mx:
        print('YES')
    else:
        print('NO')