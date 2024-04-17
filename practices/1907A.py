t = int(input())

for _ in range(t):
    s = input().strip()
    col = s[0]
    row = s[1]

    COLS = "abcdefgh"
    ROWS = "12345678"

    for i in range(8):
        if row != ROWS[i]:
            print(col + ROWS[i])
    
    for i in range(8):
        if col != COLS[i]:
            print(COLS[i] + row)
    
