T = int(input())

for _ in range(T):
    a,b,c = map(int, input().split())

    if a < b < c:
        print('STAIR')
    elif b > a and b > c:
        print('PEAK')
    else:
        print('NONE')