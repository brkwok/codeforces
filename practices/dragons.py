s, n = map(int, input().strip().split())

dragons = []

for _ in range(n):
    dragon_strength, bonus = map(int, input().strip().split())
    dragons.append((dragon_strength, bonus))

dragons.sort()

for ds, b in dragons:
    if s <= ds:
        print("NO")
        break
    s += b
else:
    print("YES")