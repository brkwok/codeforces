T = int(input().strip())

for _ in range(T):
    N = int(input().strip())
    S = input().strip()
    pref1 = [0] * (N + 1)
    pref0 = [0] * (N + 1)

    for i, ch in enumerate(S):
        pref1[i + 1] = pref1[i] + (ch == '1')
        pref0[i + 1] = pref0[i] + (ch == '0')
    
    res = []

    for i in range(N + 1):
        left_pref = pref0[i]
        right_pref = pref1[N] - pref1[i]

        if left_pref >= (i + 1) // 2 and right_pref >= (N - i + 1) // 2:
            res.append(i)

    mn = float('inf')
    mn_idx= 0

    for idx in res:
        if abs(N - 2 * idx) < mn:
            mn = abs(N - 2 * idx)
            mn_idx = idx

    print(mn_idx)