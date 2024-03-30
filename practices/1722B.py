t = int(input())

for _ in range(t):
    n = int(input())
    s1 = input().strip()
    s2 = input().strip()

    for i in range(n):
        if (s1[i] == 'R' and s2[i] != 'R') or (s1[i] != 'R' and s2[i] == 'R'):
            print("NO")
            break
    else:
        print('YES')