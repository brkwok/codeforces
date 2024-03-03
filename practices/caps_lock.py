s = input().strip()

# all upper
if s.upper() == s:
    print(s.lower())
elif s[1:].upper() == s[1:]:
    print(s[0].upper() + s[1:].lower())
else:
    print(s)
