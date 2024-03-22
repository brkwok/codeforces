T = int(input().strip())

def max_sum(nums):
    res = nums[0]

    curr = 0

    for n in nums:
        curr += n
        res = max(res, curr)
        
        if curr < 0:
            curr = 0

    return res

MOD = 10**9 + 7
for _ in range(T):
    N, K = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))

    mx = max_sum(A)
    s = sum(A)

    if mx <= 0:
        print(s % MOD)
    else:
        if K == 1:
            print((mx + s) % MOD)
        else:
            res = mx
            curr = mx

            for _ in range(K):
                res += curr
                curr += curr
                curr = curr % MOD

            print((s + res - mx) % MOD)