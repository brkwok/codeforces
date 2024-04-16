t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    mnIdx, mxIdx = 0, 0

    for i in range(n):
        if a[i] < a[mnIdx]:
            mnIdx = i
        if a[i] > a[mxIdx]:
            mxIdx = i

    leftMost, rightMost = min(mnIdx, mxIdx), max(mnIdx, mxIdx)
    movesLeft = rightMost + 1
    movesRight = n - leftMost
    movesRightFromLeft = leftMost + 1 + n - rightMost
    print(min(movesLeft, movesRight, movesRightFromLeft))