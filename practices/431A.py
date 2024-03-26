a = list(map(int, input().split()))
s = input().strip()

res = 0

for ch in s:
    res += a[int(ch) - 1]

print(res)