n = int(input())
a = list(map(int, input().split()))

res = 0
prev = 0
streak = 0

for n in a:
    if n > prev:
        streak += 1
    else:
        streak = 1

    res = max(res, streak)
    prev = n

print(res)