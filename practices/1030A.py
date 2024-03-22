N = int(input().strip())
A = map(int, input().strip().split())

for n in A:
    if n == 1:
        print("HARD")
        break
else:
    print("EASY")