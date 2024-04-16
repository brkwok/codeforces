"""
Filename: 978B.py
"""

n = int(input())
s = input().strip()

toRemove = 0
streak = 0

for ch in s:
    if ch == 'x':
        streak += 1

        if streak > 2:
            toRemove += 1
    else:
        streak = 0

print(toRemove)