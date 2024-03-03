N = int(input().strip())

A = [4,7]
prev = 0

for i in range(2):
    curr = len(A)
    for j in range(prev, curr):
        A.append(A[j] * 10 + 4)
        A.append(A[j] * 10 + 7)
    prev = curr

for num in A:
    if N % num == 0:
        print("YES")
        break
else:
    print("NO")
