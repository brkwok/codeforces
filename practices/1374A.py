T = int(input())

for _ in range(T):
    x, y, n = map(int, input().strip().split())

    mod = n % x

    if mod == y:
        print(n)
    elif mod > y:
        print(n - (mod - y))
    else:
        print(n + (y - mod) - x)
        