t = int(input())

for _ in range(t):
    s = input().strip()
    zeros = s.count('0')
    ones = s.count('1')

    if zeros == 0 or ones == 0:
        print(0)
    else:
        if zeros == ones:
            print(zeros - 1)
        else:
            print(min(zeros, ones))