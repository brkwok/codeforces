t = int(input())

for _ in range(t):
    n = int(input())

    sqrt = int(n ** 0.5)
    cubert = int(n ** (1/3))
    intersection = int(n ** (1/6))

    if (cubert+1) **3 <= n:
        cubert += 1
    if (sqrt+1) ** 2 <= n:
        sqrt += 1
    if (intersection+1) ** 6 <= n:
        intersection += 1

    print(sqrt + cubert - intersection)