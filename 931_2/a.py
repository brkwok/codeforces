T = int(input().strip())

for _ in range(T):
    N = int(input().strip())
    A = sorted(map(int, input().strip().split()))

    mx1 = abs(A[0] - A[-1])
    mx2 = abs(A[1] - A[-2])
    print(mx1 * 2 + mx2 * 2)