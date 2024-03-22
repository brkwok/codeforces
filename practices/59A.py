C = input().strip()

lower = 0
upper = 0

for c in C:
    if c.islower():
        lower += 1
    else:
        upper += 1

if lower >= upper:
    print(C.lower())
else:
    print(C.upper())