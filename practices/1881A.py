t = int(input())

for _ in range(t):
    n,m = map(int, input().split())
    x = input()
    s = input()

    if s in x:
        print(0)
    else:
        
        for i in range(10):
            x = x + x

            if s in x:
                print(i + 1)
                break
        else:
            print(-1)