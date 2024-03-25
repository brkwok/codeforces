n = int(input())
A = list(map(int, input().split()))

l, r = 0, n - 1

a = b = 0

turn = 0

while l <= r:
    if turn == 0:
        if A[l] > A[r]:
            a += A[l]
            l += 1
        else:
            a += A[r]
            r -= 1
    else:
        if A[l] > A[r]:
            b += A[l]
            l += 1
        else:
            b += A[r]
            r -= 1
    turn = (turn + 1) % 2

print(a, b)