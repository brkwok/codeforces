t = int(input())

for _ in range(t):
    s = input().strip()

    l = r = -1

    for i in range(len(s)):
        if s[i] == "a":
            l = i - 1
            r = i + 1
            break
    else:
        print("NO")
        continue

    for i in range(1, len(s)):
        if l >= 0 and s[l] == chr(ord('a') + i):
            l -= 1
        elif r < len(s) and s[r] == chr(ord('a') + i):
            r += 1
        else:
            print("NO")
            break
    else:
        print("YES")