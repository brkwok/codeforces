t = int(input())

CHARS = "0abcdefghijklmnopqrstuvwxyz"
for _ in range(t):
    n = int(input())

    if n > 53:
        print(CHARS[n - 52] + CHARS[26] + CHARS[26])
    elif n > 28:
        print(CHARS[1] + CHARS[n - 26 - 1] + CHARS[26])
    else:
        print(CHARS[1] + CHARS[1] + CHARS[n - 2])