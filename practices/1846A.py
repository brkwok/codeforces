t = int(input())

for _ in range(t):
    rope_count = 0

    n = int(input())

    for i in range(n):
        a,b = map(int, input().split())

        if a > b:
            rope_count += 1

    print(rope_count)