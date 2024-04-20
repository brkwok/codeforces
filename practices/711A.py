n = int(input())

seats = []

for _ in range(n):
    s = input()
    seats.append(s)

for i in range(n):
    if seats[i][:2] == "OO":
        seats[i] = "++" + seats[i][2:]
        print("YES")
        break
    elif seats[i][3:] == "OO":
        seats[i] = seats[i][:3] + "++"
        print("YES")
        break
else:
    print("NO")
    exit()

for i in range(n):
    print(seats[i])