t = int(input())

for _ in range(t):
    l, r = map(int, input().split())

    if l * 2 > r:
        print(r % l)
    else:
        print(r//2 - (r % 2 == 0))