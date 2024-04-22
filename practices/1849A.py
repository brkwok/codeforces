t = int(input())

for _ in range(t):
    b,c,h = map(int, input().split())
    fillings = c + h

    if b > fillings:
        print(fillings + fillings + 1)
    else:
        print(b + b - 1)