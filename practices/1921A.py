t = int(input())

for _ in range(t):
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    x4, y4 = map(int, input().split())

    side = max(abs(x1 - x2), abs(y1 - y2))

    print(side ** 2)