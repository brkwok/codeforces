N = int(input().strip())
A = list(map(int, input().strip().split()))

res = [0] * N

for i in range(N):
    res[A[i] - 1] = i + 1

print(' '.join(map(str, res)))