t = int(input())

for _ in range(t):
    n = input().strip()

    if n[-1] in "02468":
        print(0)
    else:
        if n[0] in "02468":
            print(1)
        elif "2" in n or "4" in n or "6" in n or "8" in n:
            print(2)
        else:
            print(-1)