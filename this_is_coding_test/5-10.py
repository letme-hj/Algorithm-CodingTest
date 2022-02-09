# 음료수 얼려먹기

n, m = map(int, input().split())
frame = []
for row in range(n):
    frame.append(list(map(int, input())))

def adjacent(pos):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    adjacents = []
    for i in range(4):
        new_x = pos[0] + dx[i] 
        new_y = pos[1] + dy[i]
        if new_x <1 or new_y<1 or new_x>n or new_y>m:
            continue
        adjacents.append((new_x, new_y))
    return adjacents

def available(pos):
    return frame[pos[0]-1][pos[1]-1] == 0

icecreams = []
current = [(1,1)]
while 1:
    icecream = []
    passed = []
    if len(current)==0:
        break
    while 1:
        if len(current) == 0:
            break

        pos = current[0]
        current = current[1:]
        if not available(pos):
            if pos not in passed:
                passed.append(pos) 
            if len(icecream) == 0:
                current += adjacent(pos)
        elif pos not in icecream:
            icecream.append(pos)
            current += adjacent(pos)

    icecreams.append(icecream)

    # 이 부분을 좀더 현명하게 할 수 없을까!!
    visited = []
    for i in icecreams:
        visited += i

    breaker=False
    for i in range(1,n+1):
        for j in range(1,m+1):
            temp_pos = (i,j)
            if available(temp_pos) and temp_pos not in visited:
                current = [temp_pos]
                breaker=True
                break
        if breaker:
            break

            
print(len(icecreams))