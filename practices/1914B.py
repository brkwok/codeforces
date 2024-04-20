t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    for i in range(n - k, 0, - 1):
        print(i, end = " ")

    for i in range(n - k + 1, n + 1):
        print(i, end = " ")
    print()