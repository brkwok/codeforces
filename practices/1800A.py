t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip().lower()

    meow = []

    for i, ch in enumerate(s):
        if not meow or ch != meow[-1]:
            meow.append(ch)
        
    if len(meow) != 4 or meow[0] !='m' or meow[1] != 'e' or meow[2] != 'o' or meow[3] != 'w':
        print('NO')
    else:
        print('YES')

