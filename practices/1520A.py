T = int(input())

for _ in range(T):
    N = int(input())
    S = input().strip()
    seen = set([S[0]])
    prev = S[0]

    for i in range(1, N):
        if prev != S[i]:
            if S[i] in seen:
                print('NO')
                break
            prev = S[i]
            seen.add(S[i])
    else:
        print('YES')