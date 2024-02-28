fin = open('test.in', 'r')
fout = open('test.out', 'w')

C = int(fin.readline().strip())

from collections import defaultdict, deque

def bfs(rock_time, N, M):
    nei = [(1, 0), (0, 1)]

    q = deque([(0,0)])
    curr_time = 0

    while q:
        for i in range(len(q)):
            r, c = q.pop()
            if r == N - 1 and c == M - 1:
                return curr_time
            curr_time += 1

            
            for dx, dy in nei:
                nei_r, nei_c = r + dx, c + dy

                if (min(nei_r, nei_c) < 0 or
                    nei_r >= N or
                    nei_c >= M or
                    nei_r in rock_time[(nei_c, curr_time % N)]
                    ):
                    continue

                q.append((nei_r, nei_c))
    
    return -1

    

for c in range(C):
    N, M = map(int, fin.readline().strip().split())
    grid = [list(map(int, fin.readline().strip().split())) for i in range(N)]
    rock_time = defaultdict(set)

    for r, row in enumerate(grid):
        for c, rock in enumerate(row):
            if rock == 1:
                
                curr_row = r 
                for i in range(1, N + 1):
                    curr_row -= 1
                    if curr_row < 0:
                        curr_row = N - 1
                    key = (c, i % N)

                    rock_time[key].add(curr_row)

    res = bfs(rock_time, N, M)
    print(res)

