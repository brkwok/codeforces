PI = "314159265358979323846264338327"

t = int(input())

for _ in range(t):
    n = input().strip()

    i = 0
    res = 0

    while i < len(n):
        if n[i] == PI[res]:
            res += 1
            i += 1
        else:
            break;

    print(res)