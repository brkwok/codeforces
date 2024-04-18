t = int(input())

for _ in range(t):
    node = int(input())
    res = 0

    while node > 0:
        res += node
        node //= 2
    print(res)