n, k = map(int, input().split())

time_left = 240 - k

for i in range(1, n + 1):
    time_left -= 5 * i
    if time_left < 0:
        print(i - 1)
        break
else:
    print(n)