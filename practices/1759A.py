t: int = int(input())

for _ in range(t):
    s: str = input().strip()

    if s[0] not in "Yes":
        print("NO")
    else:
        yes = "Yes"
        currIdx = yes.find(s[0])

        for i in range(1, len(s)):
            currIdx = (currIdx + 1) % 3
            if s[i] != yes[currIdx]:
                print("NO")
                break
        else:
            print("YES")
        

