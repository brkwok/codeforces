t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)

    if s < 0 or s < n:
        print(1)
    elif s == n:
        print(0)
    else:
        print(s - n)