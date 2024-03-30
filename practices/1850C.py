t = int(input())
s = []


for i in range(t):
    grid = []
    st = []

    for _ in range(8):
        grid.append(input().strip())

    for j in range(8):
        for k in range(8):
            if grid[j][k] != '.':
                st.append(grid[j][k])

    s.append("".join(st))

for string in s:
    print(string)