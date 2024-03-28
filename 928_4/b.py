T = int(input())

for _ in range(T):
    N = int(input())
    shape = []

    for i in range(N):
        c = input().strip().count('1')
        if c:
            shape.append(c)

    if shape[0] == shape[1]:
        print("SQUARE")
    else:
        print("TRIANGLE")