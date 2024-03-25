a = sorted(list(map(int, input().split())))
l = len(a)

mid = l // 2
friend_in_middle = a[mid] if l % 2 == 1 else (a[mid - 1] + a[mid]) // 2

res = 0 

for i in range(l):
    res += abs(a[i] - friend_in_middle)

print(res)