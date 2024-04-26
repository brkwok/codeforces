t = int(input())

for _ in range(t):
    L = int(input())
    s = input().strip()

    if L < 4:
        print("NO")
        continue

    match1 = 0
    r = L - 1
    year = "2020"

    for i in range(4):
        if s[r] == year[3 - i]:
            r -= 1
            match1 += 1
        else:
            break

    
    for i in range(4):
        if s[i] == year[i]:
            match1 += 1
        else:
            break;

    if match1 >=4:
        print("YES")
    else:
        print("NO")