t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    if a > b:
        a, b = b, a

    if a * 2 <= b:
        print(b ** 2)
    else:
        print((a * 2) ** 2)