T = int(input())

for _ in range(T):
    n = int(input())

    n1 = 0
    n2 = 0
    for _ in range(3):
        n1 += n % 10
        n //= 10

    for _ in range(3):
        n2 += n % 10
        n //= 10  

    if n1 == n2:
        print('YES')
    else:
        print('NO')