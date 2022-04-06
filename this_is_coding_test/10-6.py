# 위상 정렬

from collections import deque

v, e = map(int, input().split())

# 진입차수
indegree = [0] * (v+1)

# 그래프
graph = [[] for i in range(v+1)]

# 방향 그래프 모든 간선 정보 입력
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1 # b로 가는 edge니까 b의 진입차수 증가

# 위상정렬 함수
def topology_sort():
    result = [] # 순서대로 쌓을 리스트
    q = deque()

    # 진입차수 0 인 노드 먼저 큐에 들어감
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:

        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
        # graph에서 해당 노드 지워줘야하나...?
        # popleft로 이미 빼고 시작하니까 괜찮음 + cycle 아닌 경우로 전제하므로 끝은 있음!

    for i in result:
        print(i, end=' ')

topology_sort()


