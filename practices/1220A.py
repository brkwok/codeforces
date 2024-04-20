l = int(input())
s = input()

zeroCount, oneCount = 0, 0

for ch in s:
    if ch == "z":
        zeroCount += 1
    elif ch == "n":
        oneCount += 1

print("1 " * oneCount + "0 " * zeroCount)