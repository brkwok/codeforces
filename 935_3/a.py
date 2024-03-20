from math import ceil

T = int(input().strip())

for _ in range(T):
    I, E, U = map(int, input().strip().split())

    E2 = E // 3 + 1
    E_E = E % 3

    
    if E_E == 0:
        print(I + E // 3 + ceil(U / 3))
    elif U < 3 - E_E:
        print(-1)
    else:
        U -= 3 - E_E
        print(I + E2 + ceil(U / 3))