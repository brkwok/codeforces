t = int(input())

for _ in range(t):
    n = int(input())

    sq = []

    for i in range(n):
        sq.append(list(input()))

    flag = False
    x1 = y1 = x2 = y2 = 0
    for i in range(n):
        for j in range(n):
            if sq[i][j] == "*":
                if not flag:
                    x1 = i
                    y1 = j
                    flag = True
                else:
                    x2 = i
                    y2 = j
                    break

    ax1 = x1
    ax2 = x2
    ay1 = y2
    ay2 = y1
    if x1 == x2:
        if x1 == n - 1:
            ax1 = x1 - 1
            ax2 = x2 - 1
        else:
            ax1 = x1 + 1
            ax2 = x2 + 1

    if y1 == y2:
        if y1 == n - 1:
            ay1 = y1 - 1
            ay2 = y2 - 1
        else:
            ay1 = y1 + 1
            ay2 = y2 + 1

    sq[ax1][ay1] = "*"
    sq[ax2][ay2] = "*"

    for i in range(n):
        print("".join(sq[i]))
