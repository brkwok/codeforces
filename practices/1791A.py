chars = set(list('codeforces'))
T = int(input())

for _ in range(T):
    ch = input().strip()

    if ch in chars:
        print("YES")
    else:
        print("NO")