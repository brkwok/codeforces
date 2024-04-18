t = int(input())

for _ in range(t):
    n = int(input())

    if n == 1:
        print(2)
    else:
        if n % 3 == 0:
            print(n // 3)
        else:
            print(n // 3 + 1)