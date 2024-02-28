T = int(input().strip())

for i in range(T):
    A, B, L = map(int, input().strip().split())

    if L % A != 0 and L % B != 0:
        print(1)
    else:
        a, b = [], []
        res = set()
        p = 1
        while p <= L:
            a.append(p)
            p *= A

        p = 1
        while p <= L:
            b.append(p)
            p *= B

        for n in a:
            for m in b:
                val = n * m
                if L % val == 0:
                    res.add(val)
        
        print(len(res))
