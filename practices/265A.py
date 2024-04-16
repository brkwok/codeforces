INIT = input().strip()
COMMANDS = input().strip()

i = j = 0

while i < len(INIT) and j < len(COMMANDS):
    if INIT[i] == COMMANDS[j]:
        i += 1
    j += 1

print(i + 1)