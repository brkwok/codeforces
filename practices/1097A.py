t = set(list(input().strip()))

h = list(input().strip().split())

for c in h:
    rank, suit = c[0], c[1]

    if rank in t or suit in t:
        print("YES")
        break
else:
    print("NO")