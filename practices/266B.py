L, K = map(int, input().strip().split())
S = list(input().strip())

for _ in range(K):
    i = 0
    change = 0
    while i < L - 1:
        if S[i] == 'B' and S[i + 1] == 'G':
            change +=1
            S[i], S[i + 1] = S[i + 1], S[i]
            i += 2
        else:
            i += 1

    if change == 0:
        break
    
print(''.join(S))
