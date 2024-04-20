t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    mn = min(a)
    mnCount = a.count(mn)
    print(n - mnCount)