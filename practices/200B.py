N = int(input().strip())
J = list(map(int, input().strip().split()))

oj = 0

for j in J:
    oj += j

print(oj / N)