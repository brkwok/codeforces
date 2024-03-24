money = int(input().strip())

notes = [100, 20, 10, 5, 1]

count = 0

for note in notes:
    count += money // note
    money %= note

print(count)