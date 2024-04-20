t = int(input())

for _ in range(t):
    key = int(input())
    doors = list(map(int, input().split()))
    
    if key == 0:
        print("NO")
    else:
        opened = 0

        while key > 0:
            key = doors[key - 1]
            opened += 1
        if opened == 3:
            print("YES")
        else:
            print("NO")

