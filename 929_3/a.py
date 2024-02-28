T = int(input().strip())

for i in range(T):
    N = int(input().strip())
    l = map(abs,map(int, input().strip().split()))

    print(sum(l))