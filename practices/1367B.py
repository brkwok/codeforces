T = int(input())

for _ in range(T):
    N = int(input())
    A = map(int, input().strip().split())

    even_wrong = 0
    odd_wrong = 0

    for i, n in enumerate(A):
        if i % 2 == 0 and n % 2 != 0:
            even_wrong += 1
        elif i % 2 == 1 and n % 2 != 1:
            odd_wrong += 1

    if even_wrong == odd_wrong:
        print(even_wrong)
    else:
        print('-1')
