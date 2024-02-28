T = int(input().strip())

for i in range(T):
    N = int(input().strip())
    L = list(map(int, input().strip().split()))
    S = sum(L)

    if S % 3 == 0:
        print(0)
        continue
    if (S + 1) % 3 == 0:
        print(1)
        continue
    found = False
    for n in L:
        if (S - n) % 3 ==0:
            print(1)
            found = True
            break
    else:
        if not found:
            print(2)
