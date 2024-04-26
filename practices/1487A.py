t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    i = 0

    while i < n - 1 and a[i] == a[i + 1]:
        i += 1

    print(n - i - 1)