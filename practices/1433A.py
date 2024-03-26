T = int(input())

boring = [int(str(i) * j) for i in range(1, 10) for j in range(1, 5)]


for _ in range(T):
    answered = int(input())

    count = 0
    for i in range(len(boring)):
        count += i % 4 + 1

        if boring[i] == answered:
            break

    print(count)
