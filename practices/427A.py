N = int(input())
A = list(map(int, input().split()))

police = 0
crimes = 0

for n in A:
    if n > 0:
        police += n
    else:
        if police > 0:
            police -= 1
        else:
            crimes += 1

print(crimes)