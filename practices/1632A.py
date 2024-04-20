t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    if n > 2:
        print("NO")
    elif n == 2:
        if s[0] == s[1]:
            print("NO")
        else:
            print("YES")
    else:
        print("YES")