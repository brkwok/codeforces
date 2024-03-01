s1 = input().strip().lower()
s2 = input().strip().lower()

for ch1, ch2 in zip(s1, s2):
    if ch1 != ch2:
        if ch1 < ch2:
            print('-1')
        elif ch1 > ch2:
            print('1')
        break
else:
    print(0)