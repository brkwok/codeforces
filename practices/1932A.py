t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    coins = 0

    for i, ch in enumerate(s):
        if ch == ".":
            continue
        elif ch == "@":
            coins += 1
        else:
            if i < n - 1 and s[i + 1] == "*":
                break
    
    print(coins)