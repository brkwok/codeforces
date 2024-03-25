k, r = map(int, input().split())

for i in range(1, 10):
    cost = k * i

    if cost % 10 == 0 or cost % 10 == r:
        print(i)
        break
else:
    print(10)