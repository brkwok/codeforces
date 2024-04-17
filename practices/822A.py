a, b = map(int, input().split())

mn = min(a,b)

ans = 1

for i in range(1, mn+1):
    ans *= i

print(ans)