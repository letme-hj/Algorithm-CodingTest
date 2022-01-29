n = int(input())
map = input().split()

# start = [1,1]
# for dir in map:
#     if dir=='U':
#         if start[0]==1:
#             continue
#         start[0] -= 1
#     elif dir == "D":
#         if start[0]==n:
#             continue
#         start[0] += 1
#     elif dir =='L':
#         if start[1]==1:
#             continue
#         start[1] -= 1
#     elif dir=='R':
#         if start[1]==n:
#             continue
#         start[1] += 1

# print("final position:", start)


# 다른 방식 (책 풀이 참고)
dirs = {"U": (0, -1), "D": (0, 1), "R": (1, 1), "L": (1, -1)}

pos = [1,1]
for dir in map:
    dim = dirs[dir][0]
    move = dirs[dir][1]
    next_pos = pos[dim] + move
    if next_pos<1 or next_pos>n :
        continue
    pos[dim] = next_pos

print("final position:", pos)
