t = int(input())

for _ in range(t):
    tic = []

    for i in range(3):
        tic.append(input().strip())

    if tic[0][0] != "." and tic[0][0] == tic[0][1] == tic[0][2]:
        print(tic[0][0])
    elif tic[1][0] != "." and tic[1][0] == tic[1][1] == tic[1][2]:
        print(tic[1][0])
    elif tic[2][0] != "." and tic[2][0] == tic[2][1] == tic[2][2]:
        print(tic[2][0])
    elif tic[0][0] != "." and tic[0][0] == tic[1][0] == tic[2][0]:
        print(tic[0][0])
    elif tic[0][1] != "." and tic[0][1] == tic[1][1] == tic[2][1]:
        print(tic[0][1])
    elif tic[0][2] != "." and tic[0][2] == tic[1][2] == tic[2][2]:
        print(tic[0][2])
    elif tic[0][0] != "." and tic[0][0] == tic[1][1] == tic[2][2]:
        print(tic[0][0])
    elif tic[0][2] != "." and tic[0][2] == tic[1][1] == tic[2][0]:
        print(tic[0][2])
    else:
        print("DRAW")