num: int = int(input())

res: list[list[int]] = [[1] * num for _ in range(num)]

for i in range(1, num):
    for j in range(1, num):
        res[i][j] = res[i - 1][j] + res[i][j - 1]

print(res[num - 1][num - 1])
