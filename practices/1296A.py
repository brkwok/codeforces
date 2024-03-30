t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    even = False
    odd = False

    for i in a:
        if i % 2 == 0:
            even = True
        else:
            odd = True

        if even and odd:
            break

    if n % 2 == 0:
        if even and odd:
            print("YES")
        else:
            print("NO")
    else:
        if odd:
            print("YES")
        else:
            print("NO")

