t = int(input())

for _ in range(t):
    board = []
    for i in range(10):
        board.append(input().strip())

    score = 0

    for i in range(10):
        for j in range(10):
            if board[i][j] == 'X':
                if 4 <= i <= 5 and 4 <= j <= 5:
                    score += 5
                elif 3 <= i <= 6 and 3 <= j <= 6:
                    score += 4
                elif 2 <= i <= 7 and 2 <= j <= 7:
                    score += 3
                elif 1 <= i <= 8 and 1 <= j <= 8:
                    score += 2
                else:
                    score += 1

    print(score)