t = int(input())

for _ in range(t):
    s = input().strip()

    firstOne = s.find("1")
    lastOne = s.rfind("1")

    if firstOne == -1:
        print(0)
    else:
        zeroCount = s[firstOne:lastOne+1].count('0')
        print(zeroCount)