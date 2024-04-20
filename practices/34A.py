n = int(input())
a = list(map(int, input().split()))

mnDiff = []

for i in range(n - 1):
    mnDiff.append(abs(a[i] - a[i + 1]))

mnDiff.append(abs(a[0] - a[-1]))

mn = min(mnDiff)
idx = mnDiff.index(mn)

if idx == n - 1:
    print(n, 1)
else:
    print(idx + 1, idx + 2)