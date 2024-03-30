t = int(input())

for _ in range(t):
    n = int(input())
    a = set(map(int, input().split()))

    if n == len(a):
        print('YES')
    else:
        print('NO')