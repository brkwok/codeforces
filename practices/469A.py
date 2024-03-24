N = int(input().strip())

p, *p_levels = map(int, input().split())
q, *q_levels = map(int, input().split())

s = set(p_levels + q_levels)

if len(s) == N:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')