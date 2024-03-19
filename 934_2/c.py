from collections import Counter

T = int(input().strip())

for _ in range(T):
    N = int(input().strip())
    A = map(int, input().strip().split())

    C = [0] * (N + 1)

    for n in A:
        C[n] += 1

    c = 0
    for i in range(N + 1):
        if C[i] == 1:
            c += 1
        
        if C[i] == 0 or c == 2:
            print(str(i))
            break

    