s = input().strip()

totalQ = s.count('Q')
res =  0
currQ = 0
for i, ch in enumerate(s):
    currQ += ch == 'Q'
    if ch == 'A':
        res += currQ * (totalQ - currQ)

print(res)