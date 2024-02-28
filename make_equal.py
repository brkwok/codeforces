T = int(input().strip())

for i in range(T):
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    S = sum(A)
    E = S // N

    if S % N > 0:
        print("NO")
    else:
        can_give = 0
        
        for n in A:
            if n > E:
                can_give += n - E
            else:
                need = E - n

                if can_give < need:
                    print("NO")
                    can_give = -1
                    break
                else:
                    can_give -= need
        
        if can_give == -1:
            continue
        
        if can_give == 0:
            print("YES")
        else:
            print("NO")
    

