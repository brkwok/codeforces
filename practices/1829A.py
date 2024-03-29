t = int(input())
check = "codeforces"
for _ in range(t):
    s = input().strip()
    
    diff = 0
    for i in range(len(check)):
        if check[i] != s[i]:
            diff += 1
    
    print(diff)