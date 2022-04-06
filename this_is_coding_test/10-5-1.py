# 크루스칼 알고리즘
# 하나의 그래프에서 최소 비용으로 모든 노드 연결하는 부분그래프를 찾을 것 (최소비용 신장트리)


def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b
    
v, e = map(int, input().split())
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

# 전체 간선 리스트 입력받을 리스트, 최종 비용
edges = []
result = 0

for i in range(e):
    a, b, cost = map(int, input().split()) # 두 노드 뿐만 아니라 두 노드 간 간선의 비용도 받음
    edges.append((cost, a, b)) # cost 기준으로 정렬되길 원하므로 튜플의 첫번째 원소로 설정

edges.sort() # edge 내 튜플들의 첫번째 원소 기준으로 정렬됨 (오름차순)
            # (a, b)에 대해서도 이차적으로 정렬되긴 하겠지... 사전처럼

for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent, a, b)
        result += cost

print('최종 비용')
print(result)