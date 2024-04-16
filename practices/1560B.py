t = int(input())

for _ in range(t):
    a,b,c = map(int,input().split())

    numPeople = abs(a - b) * 2

    if c > numPeople or a > numPeople or b > numPeople:
        print(-1)
    else:
        if (c + numPeople // 2) % numPeople == 0:
            print(numPeople)
        else:
            print((c + numPeople // 2) % numPeople)