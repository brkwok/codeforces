T = int(input().strip())

for _ in range(T):
    N = int(input().strip())
    A = list(map(int, input().strip().split()))

    for i in range(N - 2):
        n1, n2, n3 = A[i], A[i + 1], A[i + 2]

        if n1 == 0:
            continue
        if n1 * 2 > n2 or n1 > n3:
            print("NO")
            break
        else:
            A[i] = 0
            A[i + 1] -= n1 * 2
            A[i + 2] -= n1
    else:
        if all(x == 0 for x in A):
            print("YES")
        else:
            print("NO")