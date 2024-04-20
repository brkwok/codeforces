t = int(input())

for _ in range(t):
    s = list(input().strip())

    s.sort()
    print("".join(s))
