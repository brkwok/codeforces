t = int(input())

for _ in range(t):
    counts = [0] * 26
    n = int(input())

    for i in range(n):
        s = input().strip()

        for ch in s:
            counts[ord(ch) - ord('a')] += 1
        
    print("YES" if all(count % n == 0 for count in counts) else "NO")

