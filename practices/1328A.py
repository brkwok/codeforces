T = int(input().strip())

for _ in range(T):
    A, B = map(int, input().strip().split())

    if A % B == 0:
        print(0)
    else:
        print(B - (A % B))