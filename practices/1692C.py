t = int(input())

for _ in range(t):
    # empty line
    input()
    l = []

    for i in range(8):
        l.append(input().strip())
    
    for i in range(8):
        for j in range(8):
            if l[i][j] == '#':
                if i == 0:
                    if j > 0 and j < 7 and l[i + 1][j - 1] == "#" and l[i+1][j+1] == "#":
                        print(i + 1, j + 1)
                elif i == 7:
                    if j > 0 and j < 7 and l[i - 1][j - 1] == "#" and l[i-1][j+1] == "#":
                        print(i + 1, j + 1)
                elif j == 0:
                    if i > 0 and i < 7 and l[i - 1][j + 1] == "#" and l[i+1][j+1] == "#":
                        print(i + 1, j + 1)
                elif j == 7:
                    if i > 0 and i < 7 and l[i - 1][j - 1] == "#" and l[i+1][j-1] == "#":
                        print(i + 1, j + 1)
                else:
                    if l[i - 1][j - 1] == "#" and l[i - 1][j + 1] == "#" and l[i + 1][j - 1] == "#" and l[i + 1][j + 1] == "#":
                        print(i + 1, j + 1)

    