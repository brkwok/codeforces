t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    if n % 2 == 0 or n % k == 0 or (k < n and k % 2 == n % 2):
        print("YES")
    else:
        print("NO")