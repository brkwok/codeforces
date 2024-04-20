t = int(input())

for _ in range(t):
    l1, l2 ,l3 = sorted(map(int, input().split()))

    if l1 + l2 == l3:
        print("YES")
    elif l2 == l3:
        if l1 % 2 == 0:
            print("YES")
        else:
            print("NO")
    elif l1 == l2:
        if l3 % 2 == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
