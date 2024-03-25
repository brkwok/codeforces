from collections import Counter
A = input()
B = input()
C = Counter(list(input()))


for ch in A:
    C[ch] -= 1

for ch in B:
    C[ch] -= 1

for v in C.values():
    if v != 0:
        print("NO")
        break
else:
    print("YES")