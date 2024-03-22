
K, N, W = map(int, input().strip().split())

need = (W * (W + 1) // 2) * K
print(max(0, need - N))