t = int(input())

for _ in range(t):
    s = list(input())

    turn = 0

    for i in range(len(s)):
        if turn == 0:
            if s[i] == 'a':
                s[i] = 'b'
            else:
                s[i] = 'a'
            turn = 1
        else:
            if s[i] == 'z':
                s[i] = 'y'
            else:
                s[i] = 'z'
            turn = 0

    print("".join(s))