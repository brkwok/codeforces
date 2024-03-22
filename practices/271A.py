Y = int(input().strip())

while True:
    Y += 1
    a = Y // 1000
    b = (Y // 100) % 10
    c = (Y // 10) % 10
    d = Y % 10

    if a != b and a != c and a != d and b != c and b != d and c != d:
        print(Y)
        break