r,c = map(int, input().split())

rows = [0] * r
cols = [0] * c

for i in range(r):
    row = input()
    for j in range(c):
        if row[j] == 'S':
            rows[i] = 1
            cols[j] = 1

print(r * c - sum(rows) * sum(cols))