l = int(input())
s = input()

left = 0
right = 0

for ch in s:
    if ch == 'L':
        left += 1
    else:
        right += 1

print(right + left + 1)