L = int(input().strip())
S = input().strip()
a_count = S.count('A')
d_count = L - a_count

if a_count > d_count:
    print("Anton")
elif a_count < d_count:
    print("Danik")
else:
    print("Friendship")