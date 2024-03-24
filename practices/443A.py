s = input().strip()[1:-1].split(', ')

if s[0] == '':
    print(0)
else:
    a = set(s)
    print(len(a))