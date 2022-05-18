# 유기농 배추
from collections import deque

T = int(input())

result = None

# def bfs(start, m, n, visited):
#     x, y = start
#     new = []
#     # while True:

#     if y != 0 and [x,y-1] not in visited:
#         # north
#         visited.append([x, y-1])
#         new.append([x, y-1])
#     if y != n-1 and [x, y+1] not in visited:
#         # south
#         visited.append([x, y+1])
#         new.append([x, y+1])
#     if x != 0 and [x-1, y] not in visited:
#         # west
#         visited.append([x-1, y])
#         new.append([x-1, y])
#     if x != m-1 and [x+1, y] not in visited:
#         # east
#         visited.append([x+1, y])
#         new.append([x+1, y])
    
#     return new, m, n, visited

dx = [0,0,1,-1] # 북 남 동 서
dy = [1,-1,0,0]

def bfs(graph, a, b):
    queue = deque()
    queue.append((a,b))
    graph[b][a] = 0

    while queue:
        x, y = queue.popleft() # for 문 돌리기엔 역할이 애매-할 때 queue 효과적...
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=M or ny<0 or ny>=N:
                continue
            if graph[ny][nx]==1:
                graph[ny][nx] = 0
                queue.append((nx, ny))
    return

result = []

for i in range(T):
    M, N, K = map(int, input().split()) # 1~50, 1~50, 1~2500
    print('두번째 K', K)
    # input()
    count = 0
    graph = [[0]*M for _ in range(N)]

    # print(graph)
    # input()
    for k in range(K):
        x, y = map(int, input().split())
        # print('what', what)
        # input()
        graph[y][x] = 1
    
    ##### 여기까지 입력 #####

    for a in range(N):
        for b in range(M):
            if graph[a][b] == 1:
                bfs(graph, b, a) # 여기서 다 0으로 바꿔주기 때문에 for문 돌면서 중복되는 배추뭉치 만날 일은 없음!
                count += 1
    
    result.append(count)

for i in result:
    print(i)


    #     pos.append(list(map(int, input().split()))) # 중복되는 위치는 없음 (0~M-1 | 0~N-1)
    
    # visited = []
    # news = []
    # count = 0
    # while True:
    #     if len(visited)==K:
    #         break

    #     for x ,y in pos:
    #         # bfs : 연결된 애들을 visited에 추가해주는 작업...
    #         if [x,y] not in visited:
    #             new, _, _, visited = bfs([x, y], M, N, visited)
            
    #             news.extend(new)

    #     if len(news)==0:
    #         count += 1
        
    #     pos = news
    #     news = []


    # for x, y in pos:
    #     if [x,y] not in visited:
    #         news = []
    #         while True:
    #             if len(visited) == K:
    #                 break
    #             new, _, _, visited = bfs([x,y], M, N, visited)
    #             news.extend(new)

                
    #         if len(news) ==0:
    #             break
    #         for 
                
                
                

    #         new, _, _, visited = bfs([x,y], M, N, visited)
    #         news.extend(new)
            




### 윤현
#dfs 사용 
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

t = int(input())

def dfs(x,y):
    if x <=-1 or y<=-1 or x>=m or y>=n:
        return False

    if graph[x][y] == 1 :
        graph[x][y] = 0 
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True 
    return False 

for _ in range(t):
    result = 0 

    n,m,k = map(int,input().split())
    graph = [[0]*n for _ in range(m)]
    
    
    for _ in range(k):
        a,b = map(int,input().split())
        graph[b][a] = 1
    
    for i in range(m):
        for j in range(n):
            if dfs(i,j) == True:
                result+=1 
    print(result)
              

