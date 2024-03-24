N = int(input().strip())

groups = 0
prev = None

for _ in range(N):
    magnets = input()

    if prev != magnets:
        groups += 1
        prev = magnets
    

print(groups)