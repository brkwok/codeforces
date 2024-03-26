T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    mx = max(A)
    mn = min(A)

    print(mx - mn)