# 미래도시
# 1 -> K -> X로 최대한 빠르게

from collections import defaultdict


# N, M = map(int, input().split()) # 1 <= N, M <= 100
N, M = 4,2

e = []
graph = defaultdict(list)

input_lst = [[1,3],[2,4]]

# for _ in range(M):
#     e.append(list(map(int, input().split())))
#     graph[e[-1][0]].append(e[-1][1])
#     graph[e[-1][1]].append(e[-1][0])


for i in range(M):
    e.append(input_lst[i])
    graph[e[-1][0]].append(e[-1][1])
    graph[e[-1][1]].append(e[-1][0])


# dist = [[] for i in graph]
# X, K = map(int, input().split()) # 1 <= K <= 100
X, K = 3,4

print('graph:', graph)

def shortest(node1, node2, graph):
    dist = [987654321 for _ in range(len(graph)+1)] # 0번째는 버리는 인덱스
    visited = [0 for _ in range(len(graph)+1)] # 0번째 인덱스는 버리는 인덱스
    dist[node1] = 0
    visited[node1] = 1
    visited[0] = 1
    now = node1
    while True:
        print('dist:', dist)
        print('now:', now)
        print('visited:', visited)
        input()
        if not 0 in visited or not graph[now]:
            break
        for neigh in graph[now]:
            dist[neigh] = min(dist[neigh], dist[now]+1)
        
        # 가장 거리 짧고 + 방문 안한 노드
        next_node = 0
        for node in graph:
            if dist[node] < dist[next_node] and not visited[node]:
                next_node = node
                print('update next node to:', next_node)
        
        now = next_node
        visited[now] = 1
    if dist[node2] == 987654321:
        return -1
    else:
        return dist[node2]

def func(node1, k, node2, graph):
    if -1 in [shortest(node1, k, graph), shortest(k, node2, graph)]:
        return -1
    else:
        return shortest(node1,k,graph) + shortest(node1,k,graph)

# print(shortest(1, K, graph) + shortest(K, X, graph))
print(func(1,K,X,graph))
