t = int(input())

need = set(list('vika'))

for _ in range(t):
    n, m = map(int, input().split())
    cols = [set() for i in range(m)]

    for i in range(n):
        row = input().strip()
        for j in range(m):
            if row[j] in 'vika':
                cols[j].add(row[j])

    def check():
        for i in range(m):
            for j in range(i + 1, m):
                for k in range(j + 1, m):
                    for l in range(k + 1, m):
                        if 'v' in cols[i] and 'i' in cols[j] and 'k' in cols[k] and 'a' in cols[l]:
                            return True
                        
        return False
    
    print('YES' if check() else 'NO')

        
