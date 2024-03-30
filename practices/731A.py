s = input().strip()

res = 0
curr_pos = 0

for i in range(len(s)):
    pos = ord(s[i]) - ord('a')
    res += min(abs(curr_pos - pos), 26 - abs(curr_pos - pos))
    curr_pos = pos

print(res)