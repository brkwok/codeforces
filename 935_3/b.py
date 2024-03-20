T = int(input().strip())

for _ in range(T):
    A, B, M = map(int, input().strip().split())

    print((A + M) // A + (B + M) // B)