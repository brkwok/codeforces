t = int(input())

for _ in range(t):
    a,b,c = map(int, input().split())

    a,b = min(a,b), max(a,b)
    moves = 0
    while b <= c:
        a += b
        a,b = b,a
        moves += 1
    print(moves)