from sys import stdout

T = int(input().strip())

def ask(x,y):
    print(f"? {x} {y}")
    stdout.flush()
    dist = int(input().strip())

    return dist

def ans(x,y):
    print(f"! {x} {y}")
    stdout.flush()

for _ in range(T):
    N, M = map(int, input().strip().split())

    # first query always N,N or M,M
    
    dist = ask(1,1)

    if dist == 0:
        ans(1, 1)
        continue

    curr_x = curr_y = 0
    # odd
    if dist % 2:
        half = dist // 2
        curr_x = 1 + half + 1
        curr_y = 1 + half
    else:
        curr_x = curr_y = 1 + dist // 2

    dist = ask(curr_x, curr_y)

    if dist == 0:
        ans(curr_x, curr_y)
        continue
        
    # distance has to be even now
    half = dist // 2
    poss_x1, poss_y1 = curr_x - half, curr_y + half
    poss_x2, poss_y2 = curr_x + half, curr_y + half

    if poss_x1 < 1 or poss_x1 > N or poss_y1 < 1 or poss_y1 > M:
        ans(poss_x2, poss_y2)
        continue
        
    if poss_x2 < 1 or poss_x2 > N or poss_y2 < 1 or poss_y2 > M:
        ans(poss_x1, poss_y1)
        continue

    print(f"? {poss_x1} {poss_y1}")
    dist = int(input().strip())

    if dist == 0:
        print(f"! {poss_x1} {poss_y1}")
    else:
        print(f"! {poss_x2} {poss_y2}")
    stdout.flush()

