t = int(input())

def choose(n, r):
    res = 1
    
    for i in range(r + 1, n + 1):
        res *= i

    for i in range(1, n - r + 1):
        res //= i

    return res

for _ in range(t):
    n = int(input())
    input()

    poss_nums = 10 - n

    comb = choose(poss_nums, 2)
    print(comb * 6)