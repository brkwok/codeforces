t = int(input())

for _ in range(t):
    a,b,c = map(int, input().split())
    mx = max(a,b,c)

    mxCount = int(a == mx) + int(b == mx) + int(c == mx)

    if mxCount > 1:
        a = mx - a + 1 if a < mx else 1
        b = mx - b + 1 if b < mx else 1
        c = mx - c + 1 if c < mx else 1
    else:
        a = mx - a + 1 if a < mx else 0
        b = mx - b + 1 if b < mx else 0
        c = mx - c + 1 if c < mx else 0
    
    print(a,b,c)