t = int(input())

for _ in range(t):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    total = sum(a)

    leftSeq = 0
    res = float('-inf')

    for i, num in enumerate(a[:-1]):
        leftSeq += num
        rightSeq = total - leftSeq
        leftAvg = float(leftSeq) / (i + 1)
        rightAvg = float(rightSeq) / (n - i - 1)
        res = max(res, leftAvg + rightAvg)

    print(res)