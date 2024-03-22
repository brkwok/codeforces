N = int(input().strip())

f_count = 0
s_count = 0


while N > 0:
    if N % 10 == 4:
        f_count += 1
    elif N % 10 == 7:
        s_count += 1
    N //= 10

if f_count + s_count == 4 or f_count + s_count == 7:
    print("YES")
else:
    print("NO")