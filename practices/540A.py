l = int(input())

s1 = input()
s2 = input()

moves = 0

for i in range(l):
    a = int(s1[i])
    b = int(s2[i])

    moves += min(abs(a - b), 10 - abs(a - b))

print(moves)