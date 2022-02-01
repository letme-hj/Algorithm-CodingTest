###### 입력
n, m = map(int, input().split())
row, col, dir = map(int, input().split())   # dir - 0: 북 / 1: 동 / 2: 남 / 3: 서
map_ = []
for i in range(n):
    map_row = list(map(int, input().split()))   # 0: 육지 / 1: 바다
    map_.append(map_row)

pos = [row, col]
######

# 방문한 칸 (행, 열)
visited = [pos]   
# dir 별 move (dim, moving dir)
moves = {0: (0,-1), 1: (1,1), 2: (0,1), 3: (1,-1)}   

# unavailable
is_unavailable = lambda x : x[0] >= n or x[0] < 0 or x[1] >= m or x[1] < 0
# visited
is_visited = lambda x : x in visited
# sea
is_sea = lambda x : map_[x[0]][x[1]] == 1

start_dir = dir

while 1:

    # 다음 방향으로 회전
    if dir - 1 < 0:
        next_dir = 3
    else:
        next_dir = dir - 1
    dir = next_dir

    # 현 방향으로 움직인 다음 좌표
    next_pos = pos.copy()
    next_pos[moves[dir][0]] = pos[moves[dir][0]]+moves[dir][1]

    # 현 방향이 처음 시작한 방향이라면 (한바퀴 다 돈 것)
    if dir == start_dir:
        # 뒤로 간 좌표
        back_pos = pos.copy()
        back_pos[moves[dir][0]] = pos[moves[dir][0]] - moves[dir][1]

        if is_unavailable(back_pos) or is_visited(back_pos) or is_sea(back_pos):
            print(len(visited))
            break
        pos = back_pos
        start_dir = dir
        visited.append(pos)

    else:
        if is_unavailable(next_pos) or is_visited(next_pos) or is_sea(next_pos):
            continue
        pos = next_pos
        start_dir = dir
        visited.append(pos)
