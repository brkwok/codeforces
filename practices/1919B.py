t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    plus = 0
    minus = 0

    for i in range(n):
        if s[i] == "+":
            plus += 1
        else:
            minus += 1

    print(abs(plus - minus))