t = int(input())

def cal_cost(s1: str, s2: str, m: int) -> int:
    cost = 0
    for i in range(m):
        cost += abs(ord(s1[i]) - ord(s2[i]))
    return cost

for _ in range(t):
    n,m = map(int, input().split())

    words = []

    for i in range(n):
        words.append(input())

    min_cost = m * 26

    for i in range(n):
        for j in range(i + 1, n):
            min_cost = min(min_cost, cal_cost(words[i], words[j], m))

    print(min_cost)