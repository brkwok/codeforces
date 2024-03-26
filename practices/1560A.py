T = int(input())

for _ in range(T):
    K = int(input())

    k = 0
    i = 1

    while k < K:
        if i % 3 != 0 and i % 10 != 3:
            k += 1

        i += 1

    print(i - 1)