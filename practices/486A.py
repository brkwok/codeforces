N = int(input().strip())

if N % 2 == 0:
    print(N // 2)
else:
    print(-1 * (N // 2 + 1))