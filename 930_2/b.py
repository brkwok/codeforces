T = int(input().strip())

for _ in range(T):
    D = int(input().strip())
    R1 = input().strip()
    R2 = input().strip()

    for i in range(D):
        if i == D - 1 or R1[i+1] > R2[i]:
            print(R1[:i + 1] + R2[i:])
        
            j = i - 1

            res = 1
            while j >= 0 and R2[j] == R1[j + 1]:
                j -= 1
                res += 1

            print(res)
            break