N = int(input())

home = []
away = []

for i in range(N):
    h, a = map(int, input().split())
    home.append(h)
    away.append(a)

count = 0

for i in range(N):
    count += away.count(home[i])

print(count)