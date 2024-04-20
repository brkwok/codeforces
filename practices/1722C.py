t = int(input())

for _ in range(t):
    n = int(input())
    
    points = [0] * 3
    appearedWords = {}
    for i in range(3):
        words = input().strip().split()

        for word in words:
            if word not in appearedWords:
                appearedWords[word] = []

            appearedWords[word].append(i)

    for word, appeared in appearedWords.items():
        if len(appeared) == 1:
            points[appeared[0]] += 3
        elif len(appeared) == 2:
            points[appeared[0]] += 1
            points[appeared[1]] += 1
    print(*points)