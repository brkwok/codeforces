s = input().strip()

res = []

i = 0 

while i < len(s):
    if s[i] == '.':
        res.append('0')
    elif s[i] == '-':
        if s[i + 1] == '.':
            res.append('1')
        else:
            res.append('2')

        i += 1
    i += 1

print("".join(res))