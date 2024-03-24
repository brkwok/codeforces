N = int(input().strip())
A = list(map(int, input().strip().split()))

mn, mx = min(A), max(A)

res = 0

# find last occurence of mn
for i in range(N-1, -1, -1):
    if A[i] == mn:
        break

# find first occurence of mx
for j in range(N):
    if A[j] == mx:
        break

if i < j:
    res = N - i + j - 2
else:
    res = N + j - i - 1

print(res)