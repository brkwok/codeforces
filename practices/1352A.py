T = int(input())

for _ in range(T):
    s = input()
    res = []
    
    for i, dig in enumerate(reversed(s)):
        if dig != '0':
            res.append(dig + '0' * i)

    print(len(res))
    print(" ".join(res))

