t = int(input())

for _ in range(t):
    l = int(input())
    s = input()

    charMap = {}
    curr = 0

    for ch in s:
        if ch in charMap:
            if charMap[ch] != curr:
                print("NO")
                break
        else:
            charMap[ch] = curr
            
        curr = (curr + 1) % 2
    else:
        print("YES")
        
        