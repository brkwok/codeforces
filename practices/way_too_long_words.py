T = int(input().strip())

for _ in range(T):
    s = input().strip()
    if len(s) <= 10:
        print(s)
    else:
        print(s[0] + str(len(s) - 2) + s[-1])

        

        