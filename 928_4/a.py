T = int(input())

for _ in range(T):
    s = input().strip()
    c = s.count('A')

    if c > 2:
        print('A')
    else:
        print('B')