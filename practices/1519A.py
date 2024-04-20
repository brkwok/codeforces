t = int(input())

for _ in range(t):
    r,b,d = map(int, input().split())

    if r > b:
        r,b = b,r

    if b <= r*(d+1):
        print("YES")
    else:
        print("NO")