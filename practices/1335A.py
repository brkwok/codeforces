T = int(input())

for _ in range(T):
    N = int(input())
    alice = N // 2 + 1
    betty = N - alice

    print(betty)