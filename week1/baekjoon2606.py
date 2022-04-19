# 바이러스

# ---
### [1번째 시도] 신장트리 이용하면 될 듯! 집합 묶이는...


# def find_root(root, x):
#     if root[x] != x:
#         root[x] = find_root(root, root[x])
#     return root[x]

# def update_root(root, x, y): # inplace function
#     x = find_root(root, x)
#     y = find_root(root, y)
#     if x<y:
#         root[y] = x
#     else:
#         root[x] = y

# ## 입력 받기
# n = int(input())
# connections = int(input())
# pairs = []
# for i in range(connections):
#     pairs.append(list(map(int, input().split())))

# ## 선언하고  그냥 돌리기 ㅎㅎ
# n = 7
# pairs = [[1,2], [2,3], [1,5], [5,2], [5,6], [4,7]]

# root = list(range(n+1))

# for a, b in pairs:
#     update_root(root, a, b)

# print(root.count(1)-1)

# ---
### [2번째 시도] dfs bfs를 써보자

n = int(input())
graph = [[] for _ in range(n+1)]

connections = int(input())
pairs = []
for i in range(connections):
    a, b = map(int, input().split())
    pairs.append([a,b])
    graph[a].append(b)
    graph[b].append(a)

visited = [0 for _ in range(n+1)]

def dfs(array, node, visited):
    """연결된 Node 출력. 단 visited 빼고"""
    result = [node]
    visited[node] = 1
    for i in array[node]:
        # print(f'{node}와 연결된 {i}')
        # input()
        if visited[i] == 0:
            visited[i] = 1
            # print(f'visited: {visited}')
            # input()
            result.extend(dfs(array, i, visited))
    return result
    

print(len(dfs(graph, 1, visited))-1)
