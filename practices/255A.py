n = int(input())
a = list(map(int, input().split()))

res = [0, 0, 0]

for i in range(n):
    res[i % 3] += a[i]

if res.index(max(res)) == 0:
    print("chest")
elif res.index(max(res)) == 1:
    print("biceps")
else:
    print("back")