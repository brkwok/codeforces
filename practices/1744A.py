t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = input()
    charMap = {}

    for i in range(n):
        if a[i] not in charMap:
            charMap[a[i]] = s[i]
        else:
            if charMap[a[i]] != s[i]:
                print("NO")
                break
    else:
        print("YES")