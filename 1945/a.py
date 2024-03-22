T = int(input().strip())

for _ in range(T):
    N = int(input().strip())
    S = input().strip()

    if S == S[::-1]:
        print(S)
    elif S < S[::-1]:
        if N % 2 == 0:
            print(S)
        else:
            print(S[::-1] + S)
    else:
        if N % 2 == 0:
            print(S[::-1] + S)
        else:
            print(S)