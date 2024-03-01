N = int(input().strip())
s = input().strip()

res = 0
curr = s[0]

for i in range(1, N):
    if s[i] == curr:
        res += 1
    curr = s[i]

print(res)