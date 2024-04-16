from math import sqrt

t = int(input())


for _ in range(t):
    n = int(input())
    s = sum(map(int, input().split()))

    sq = sqrt(s)
    if sq == int(sq):
        print("YES")
    else:
        print("NO")