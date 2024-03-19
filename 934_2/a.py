T = int(input().strip())

for _ in range(T):
    N, K = map(int, input().strip().split())

    out_degree = N - 1

    if K < out_degree:
        print(f'{N}')
    else:
        print("1")