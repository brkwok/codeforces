t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    xor = 0

    for num in a:
        xor ^= num

    print(xor ^ a[0])