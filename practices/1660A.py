t = int(input())

for _ in range(t):
    a,b = map(int, input().split())

    if a == 0:
        print(1)
    elif b == 0:
        print(a + 1)
    else:
        print(b * 2 + a + 1)