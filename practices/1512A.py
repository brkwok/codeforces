T = int(input())

for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))

    if a[0] != a[1] and a[1] == a[2]:
        print(1)
        continue
    elif a[-1] != a[-2] and a[-2] == a[-3]:
        print(n)
        continue

    diff = 0
    prev = a[0]

    for i in range(1, n):
        if a[i] != prev:
            diff += 1
            if diff > 1:
                print(i)
                break
        prev = a[i]


