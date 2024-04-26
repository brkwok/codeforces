t = int(input())

for i in range(t):
    a = input().strip()
    b = input().strip()

    a1= a.count('1')
    b1 = b.count('1')

    if a1 + b1 == 4:
        print(2)
    elif a1 + b1 == 0:
        print(0)
    else:
        print(1)
