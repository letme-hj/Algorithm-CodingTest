pos = input()

dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
col = dict[pos[0]]
row = int(pos[1])
pos = [col, row]
moves = [(0,-1), (0,1), (1,-1), (1,1)]

count = 0
for move in moves:
    if 0 < (pos[move[0]] + 2*move[1]) < 9:
        if move[0]: # if first move was 수직이동
            if pos[0]+1 < 9:
                count+=1
            if pos[0]-1 > 0:
                count+=1
        else: # if first move was 수평이동
            if pos[1]+1 < 9:
                count+=1
            if pos[1]-1 > 0:
                count+=1

print(count)

# 교재에서는 나이트의 이동 방향 8가지를 리스트로 정의해둠 (좌표 형식으로)