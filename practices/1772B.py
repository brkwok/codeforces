t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    c, d = map(int, input().split())

    if a < b and c < d and a < c and b < d:
        print("YES")
    elif c < a and d < b and c < d and a < b:
        print("YES")
    elif d < c and b < a and d < b and c < a:
        print("YES")
    elif b < d and a < c and b < a and d < c:
        print("YES")
    else:
        print("NO")
