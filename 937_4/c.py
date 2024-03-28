T = int(input())

for _ in range(T):
    h, m = map(int, input().strip().split(":"))
    ampm = "AM"
    if 12 <= h < 24:
        ampm = "PM"
        h -= 12
    elif h == 24:
        h = 12

    if h == 0:
        h = 12

    print(f"{h:02d}:{m:02d} {ampm}")