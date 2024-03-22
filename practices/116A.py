T = int(input().strip())

mx = 0
curr = 0
for _ in range(T):
    leaving, entering = map(int, input().strip().split())
    curr -= leaving
    curr += entering
    mx = max(mx, curr)

print(mx)
    