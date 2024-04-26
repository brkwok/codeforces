t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    seen = set(a)

    for i in b:
        if i in seen:
            print('YES')
            print(1, i)
            break
    else:
        print("NO")