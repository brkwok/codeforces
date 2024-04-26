from collections import Counter
n = int(input())
a = Counter(map(int, input().split()))

print(max(a.values()))