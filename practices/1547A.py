t = int(input())

for _ in range(t):
    #empty line
    input()
    xa, ya = map(int, input().split())
    xb, yb = map(int, input().split())
    xf, yf = map(int, input().split())

    if xa == xb and xb == xf and min(ya, yb) < yf and yf < max(ya, yb):
        print(abs(ya - yb) + 2)
    elif ya == yb and yb == yf and min(xa, xb) < xf and xf < max(xa, xb):
        print(abs(xa - xb) + 2)
    else:
        print(abs(xa - xb) + abs(ya - yb))
        