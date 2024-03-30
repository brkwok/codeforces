t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    l, r = 0, n - 1

    while l < r and s[l] != s[r]:
        l += 1
        r -= 1

    if l == r:
        print(1)
    elif l > r:
        print(0)
    else:
        print(r - l + 1)