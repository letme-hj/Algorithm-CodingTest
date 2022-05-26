# 점프 점프 
# 아직 못 품...


### 첫번째 시도
# N = int(input())
# maze = list(map(int, input().split()))


# from collections import deque

# def bfs(queue, count, done=False):
#     """
#     queue에는 인덱스가 들어감. 이동할 수 있는 후보들..!
#     """
#     count += 1
#     # print(queue)
#     # input()
    
#     # if queue.count(0)==len(queue):
#     #     queue = deque([])
#     #     return queue, count, done

#     step_len = len(queue) # 몇개 볼 건지

#     for k in range(step_len): # 현재 queue에 들어있는 모든 원소 돌 것 (count +=1 에 해당하는 거 다 부수고 간다)

#         pos = queue[0] # 첫번째에 있는 거 꺼내옴
#         if maze[pos] == 0: # 0이면 이동이 이루어질 수가 없으니까 버려야해.
#             queue.popleft()
#             continue
        
#         # 하나의 queue 원소에서 갈 수 있는 인덱스 모을 것.
#         for i in range(1, maze[pos]+1): # 그 수 이하만큼 움직일 수 있으니 (제자리에 있을 수도 있음)
#             if pos+i <= goal and pos+i not in queue: # 아직 goal 이하여야 가치가 있음 (아니면 maze 벗어나버리니까)
#                 queue.append(pos+i)
                
#             if pos+i == goal: # goal 도달해버렸으면? 당장 count 데리고 나가야해...
#                 done = True
#                 break
        
#         # 다 돌았으면 그 queue[0]은 보내주자
#         queue.popleft() 

#         if done:
#             break
        
        
#     return queue, count, done

# pos = 0
# goal = N-1
# nums = deque([pos])
# jumps = 0
# done = False

# while nums:
#     # print(nums)
#     # input()

#     nums, jumps, done = bfs(nums, jumps)
#     if done:
#         break

# if not done:
#     jumps = -1
    
# # print(nums)

# print(jumps)


### 두번째 시도 (heapq 활용)

N = int(input())
maze = list(map(int, input().split()))

goal = N-1

import heapq

lst = [(0, 0)] # 출발 지점으로 초기화 (count, index)
heapq.heapify(lst)
done = False

while lst:
    lst = list(set(lst))
    lst_inv = [(i[1], i[0]) for i in lst]
    heapq.heapify(lst_inv)
    if lst_inv[0][0]>goal:
        break
    heapq.heapify(lst)
    count, pos = heapq.heappop(lst)
    if maze[pos]==0:
        continue
    for i in range(1, maze[pos]+1):
        if pos+i == goal:
            print(count+1)
            done=True
            break
        if pos+i<goal:
            lst.append((count+1, pos+i))
            
        # if pos+i == goal:
        #     print(count+1)
        #     done=True
        #     break
    if done:
        break
    

if not done:
    print(-1)
