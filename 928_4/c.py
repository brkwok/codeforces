T = int(input())
pre = [0] * 200001

def s(i):
    res = 0
    while i > 0:
        res += i % 10
        i //= 10

    return res

for i in range(1, 200001):
    pre[i] = pre[i-1] + s(i)

for _ in range(T):
    N = int(input())
    print(pre[N])