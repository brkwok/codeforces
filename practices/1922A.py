t = int(input())

for _ in range(t):
    n = int(input())

    a = input().strip()
    b = input().strip()
    c = input().strip()

    flag = False
    for i in range(n):
        if a[i] != c[i] and b[i] != c[i]:
            flag = True
        if a[i] == b[i] and a[i] != c[i]:
            flag = True

    if flag:
        print("YES")
    else:
        print("NO")