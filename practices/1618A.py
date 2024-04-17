t = int(input())

for _ in range(t):
    a = list(map(int, input().split()))

    x,y = a[0], a[1]
    z = a[-1] - x - y

    print(x,y,z)