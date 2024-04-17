t = int(input())

for _ in range(t):
    n = int(input())
    div3 = n // 3
    mod3 = n % 3
    
    if mod3 == 0:
        print(div3, div3 + 1, div3 - 1)
    elif mod3 == 1:
        print(div3, div3 + 2, div3 - 1)
    else:
        print(div3 + 1, div3 + 2, n - 2 * div3 - 3)