N = int(input().strip())

res = []
A = 'I hate'
B = 'I love'

for i in range(N):
    if i % 2:
        res.append(B)
    else:
        res.append(A)

res[-1] = res[-1] + ' it'

print(' that '.join(res))