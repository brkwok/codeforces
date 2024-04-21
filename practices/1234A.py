t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    s = sum(a)
    avg = s // n

    print(avg + (s % n != 0))