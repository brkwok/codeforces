T = int(input().strip())

for _ in range(T):
    L = int(input().strip())
    S = input().strip()

    res = 0

    for i in range(L - 2):
        s = S[i:i + 3]
        if s == 'map' or s == 'pie':
            res += 1
    
    for i in range(L - 4):
        s = S[i:i + 5]
        if s == "mapie":
            res -= 1

    print(res)