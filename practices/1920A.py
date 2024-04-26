t = int(input())

for _ in range(t):
    n = int(input())

    gt, lt, neq = 1, 10**9 + 1, set()
    for i in range(n):
        a, x = map(int, input().split())

        if a == 1:
            gt = max(gt, x)
        elif a == 2:
            lt = min(lt, x)
        else:
            neq.add(x)

    res = lt - gt + 1
    for n in neq:
        if n >= gt and n <= lt:
            res -= 1
    
    print(max(0, res))