t = int(input())

for _ in range(t):
    a,b,c = map(int, input().split())
    c %= 2

    if a + c > b:
        print("First")
    else:
        print("Second")