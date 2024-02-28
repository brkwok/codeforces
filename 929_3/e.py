L = [0] * 100010
res = []
T = int(input().strip())

for t in range(T):
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    L[1:] = A
    
    for idx in range(1, N + 1):
        L[idx] += L[idx - 1]

    Q = int(input().strip())

    for q in range(Q):
        LO, U = map(int, input().strip().split())
        LB = L[LO - 1]

        if L[N] - LB < U:
            res.append(N)
        else:
            ans = N
            mn, mx = LO, N - 1

            while mn <= mx:
                mid = (mn + mx) // 2

                if L[mid] - LB >= U:
                    ans = mid
                    mx = mid - 1
                else:
                    mn = mid + 1
            
            
            if ans == LO:
                res.append(LO)
            else:
                v1 = L[ans] - LB
                v2 = L[ans - 1] - LB

                if v1 - U - 1 < U - v2:
                    res.append(ans)
                else:
                    res.append(ans - 1)

    print(" ".join(map(str, res)))
    res.clear()

