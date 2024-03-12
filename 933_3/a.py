T = int(input().strip())

for _ in range(T):
    N, M, K = map(int, input().strip().split())

    A1 = sorted(map(int, input().strip().split()))
    A2 = sorted(map(int, input().strip().split()))

    res = 0

    for n in A1:
        l, r = 0, M

        while l < r:
            mid = (l + r) // 2

            if A2[mid] + n > K:
                r = mid
            else:
                l = mid + 1 

        res += r if r > 0 else 0

    print(res)