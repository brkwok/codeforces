N = int(input())

m = 0
c = 0

for _ in range(N):
    m1, c1 = map(int, input().split())

    if m1 > c1:
        m += 1
    elif c1 > m1:
        c += 1

if m > c:
    print("Mishka")
elif c > m:
    print("Chris")
else:
    print("Friendship is magic!^^")