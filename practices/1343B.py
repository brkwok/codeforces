T = int(input())

for _ in range(T):
    N = int(input())

    half = N // 2

    if half % 2 != 0:
        print("NO")
    else:
        print("YES")
        even = list(range(2, N + 1, 2))
        odd = list(range(1, N - 1, 2)) + [N - 1 + half]

        print(*even, *odd)