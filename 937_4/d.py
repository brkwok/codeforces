from collections import deque

T = int(input())

s = []

def subset(l, curr):
    if l > 4:
        s.append(curr[:])
        return 
    
    curr.append('1')
    subset(l + 1, curr)
    curr.pop()

    curr.append('0')
    subset(l + 1, curr)
    curr.pop()

    return

subset(0, [])

bin_dec = [int(''.join(i)) for i in s]
bin_dec.pop()
bin_dec.pop()

for _ in range(T):
    N = input().strip()

    if N[-1] != '0' and N[-1] != '1':
        print('NO')
    elif N.count('0') + N.count('1') == len(N):
        print('YES')
    else:
        N = int(N)
        
        q = deque([N])

        found = False
        while q:
            n = q.popleft()

            if n == 1:
                print('YES')
                found = True
                break
            for bd in bin_dec:
                if n % bd == 0:
                    q.append(n // bd)
        
        if not found:
            print('NO')