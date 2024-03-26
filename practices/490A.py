N = int(input())
A = list(map(int, input().split()))

ones = []
twos = []
threes = []

for i, n in enumerate(A):
    if n == 1:
        ones.append(i + 1)
    elif n == 2:
        twos.append(i + 1)
    else:
        threes.append(i + 1)

min_len = min(len(ones), len(twos), len(threes))

print(min_len)

for i in range(min_len):
    print(ones[i], twos[i], threes[i])

