A, B, C = int(input().strip()), int(
    input().strip()), int(input().strip())

print(max(A + B + C, A * B * C, A * B + C, A + B * C, (A + B) * C, A * (B + C)))
