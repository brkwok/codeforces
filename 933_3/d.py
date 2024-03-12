T = int(input().strip())

for _ in range(T):
    N, M, X = map(int, input().strip().split())

    dp = [0] * N
    dp[X - 1 if X > 0 else N - 1] = 1

    for _i in range(M):
        dist, direction = input().strip().split()
        dist = int(dist) % N

        new_dp = [0] * N
        for i in range(N):
            if dp[i] == 1:
                if direction == "0":
                    new_dp[(i + dist) % N] = 1
                elif direction == "1":
                    new_dp[(i - dist) % N] = 1
                else:
                    new_dp[(i + dist) % N] = 1
                    new_dp[(i - dist) % N] = 1
        dp = new_dp

    res = []
    for i, n in enumerate(dp):
        if n == 1:
            res.append(i + 1)
    
    print(len(res))
    print(" ".join(map(str, res)))