n, m = map(int, input().split())

s = []

for i in range(n):
    s.append(input().strip().split())

for i in range(n):
    for j in range(m):
        if s[i][j] == 'C' or s[i][j] == 'M' or s[i][j] == 'Y':
            print('#Color')
            exit()
            

print('#Black&White')