t = int(input())

CHARS = "0abcdefghijklmnopqrstuvwxyz"

for _ in range(t):
    l = int(input())
    s = input().strip()
    stack = []

    for i,c in enumerate(s):
        if c == "0":
            if i < l - 1 and s[i+1] == "0":
                stack.append(c)
                continue
            second, first = stack.pop(), stack.pop()
            stack.append(first + second)
        else:
            stack.append(c)

    res = [CHARS[int(c)] for c in stack]

    print("".join(res))