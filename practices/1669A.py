T = int(input())

for _ in range(T):
    rating = int(input())

    if rating < 1400:
        print('Division 4')
    elif rating < 1600:
        print('Division 3')
    elif rating < 1900:
        print('Division 2')
    else:
        print('Division 1')