t = int(input())

for _ in range(t):
    comb = int(input())
    seq = list(map(int, input().split()))

    for i in range(comb):
        moves, commands = input().strip().split()
        moves = int(moves)
        for j in range(moves):
            if commands[j] == 'D':
                seq[i] = (seq[i] + 1) % 10
            else:
                seq[i] = (seq[i] - 1) % 10

    print(*seq)