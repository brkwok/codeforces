N, K = map(int, input().strip().split())

a = list(map(int, input().split()))

s = sum(1 for i in range(N) if a[i] >= a[K - 1] and a[i] > 0)
print(s)