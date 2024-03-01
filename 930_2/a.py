from math import log2

T = int(input().strip())

for _ in range(T):
    A = int(input().strip())

    n = log2(A)
    print(2**int(n))