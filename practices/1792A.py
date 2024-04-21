t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    onesCount = a.count(1)
    res = n - onesCount

    print(res + onesCount // 2 + onesCount % 2)