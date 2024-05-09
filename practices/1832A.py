t = int(input())

for _ in range(t):
    s = input().strip()
    n = len(s)

    chars = set()

    for i in range(n // 2):
        chars.add(s[i])

    if len(chars) > 1:
        print("YES")
    else:
        print("NO")