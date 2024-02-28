T = int(input().strip())

for i in range(T):
    N = int(input().strip())
    L = list(map(int, input().strip().split()))
    
    mn = min(L)
    if L.count(mn) == 1:
        print("YES")
    else:
        for n in L:
            if n % mn != 0:
                print("YES")
                break
        else:
            print("NO")