t = int(input())

for _ in range(t):
    n,m = map(int, input().split())

    if n % 2 == m % 2:
        print("Tonya")
    else:
        print("Burenka")