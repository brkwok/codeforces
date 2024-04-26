t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    for i in range(n - 1):
        if s[i] != s[i + 1]:
            print(i + 1, i + 2)
            break
    else:
        print(-1, -1)