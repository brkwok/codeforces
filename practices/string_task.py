s = input().strip().lower()

vowels = 'aeiouy'

res = []

for ch in s:
    if ch not in vowels:
        res.append(ch)

print("." + ".".join(res))