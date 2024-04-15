t = int(input())

for _ in range(t):
    a, b, c = map(int, input().strip().split())

    res1 = a - 1
    res2 = b - 1 if c <= b else c - b + (c - 1)

    if res1 == res2:
        print(3)
    elif res1 < res2:
        print(1)
    else:
        print(2)
