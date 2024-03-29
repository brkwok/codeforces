t = int(input())

for _ in range(t):
    price = int(input())

    if price % 3 == 0:
        print(price // 3, price // 3)
    elif price % 3 == 1:
        print(price // 3 + 1, price // 3)
    else:
        print(price // 3 , price // 3 + 1)