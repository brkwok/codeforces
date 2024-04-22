t = int(input())

for _ in range(t):
    n = int(input())

    s1_mn, s2_mn, both_mn = 10**9, 10**9, 10**9
    for i in range(n):
        time, skills = input().split()
        
        if skills == "11":
            both_mn = min(both_mn, int(time))
        elif skills == "10":
            s1_mn = min(s1_mn, int(time))
        elif skills == "01":
            s2_mn = min(s2_mn, int(time))

    both_mn = min(both_mn, s1_mn + s2_mn)

    if both_mn == 10**9:
        print(-1)
    else:
        print(both_mn)

