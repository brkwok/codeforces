T = int(input().strip())

for _ in range(T):
    N = int(input().strip())
    A = list(sorted(map(int, input().strip().split())))

    mid = N // 2
    target_idx = mid - 1 if N % 2 == 0 else mid
    target = A[mid] + 1 if N % 2 == 1 else ((A[mid] + A[mid - 1]) // 2) + 1

    res = 0

    for i in range(N-1, target_idx - 1, -1):
        if A[i] < target:
            res += 1

    print(res)