T = int(input().strip())

for _ in range(T):
    N = int(input().strip())
    A = list(map(int, input().strip().split()))

    S = set(A)
    mex = None
    for i in range(N + 1):
        if i not in S:
            mex = i
            break

            