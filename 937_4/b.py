T = int(input())

for _ in range(T):
    N = int(input())

    row1 = []
    row2 = []
    for i in range(N):
        if i % 2 == 0:
            row1.append("#" * 2)
            row2.append('.' * 2)
        else:
            row1.append("." * 2)
            row2.append('#' * 2)

    res = []

    s1 = "".join(row1) + '\n' + "".join(row1)
    s2 = "".join(row2) + '\n' + "".join(row2)
    for i in range(N):
        if i % 2 == 0:
            res.append(s1)
        else:
            res.append(s2)


    print("\n".join(res))