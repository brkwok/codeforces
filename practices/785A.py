N = int(input().strip())

res = 0
d = {'Tetrahedron': 4, 'Cube': 6, 'Octahedron': 8, 'Dodecahedron': 12, 'Icosahedron': 20}

for _ in range(N):
    res += d[input()]

print(res)