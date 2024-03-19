from collections import Counter
T = int(input().strip())

for _ in range(T):
    N, K = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))

    B = sorted(A[:N])
    c = Counter(B)
    a1 = []
    a2 = []

    in_b = []
    not_in_b = []
    in_both = []
    for i in range(1, N + 1):
        if c[i] == 2:
            in_b.append(i)
        elif i not in c:
            not_in_b.append(i)
        else:
            in_both.append(i)

    a1.extend(in_b[:K] * 2)
    a2.extend(not_in_b[:K] * 2)

    if len(a1) == 2 * K:
        print(" ".join(map(str, a1)))
        print(" ".join(map(str, a2)))
    else:
        a1.extend(in_both[:2 * K - len(a1)])
        a2.extend(in_both[:2 * K - len(a2)])
        print(" ".join(map(str, a1)))
        print(" ".join(map(str, a2)))



