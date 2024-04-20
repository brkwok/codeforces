t = int(input())

for _ in range(t):
    a,b,k = map(int, input().split())

    moves = a - b

    print(moves * (k // 2) + (k % 2) * a)