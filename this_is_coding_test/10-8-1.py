# 도시 분할 계획
# 출처: https://www.acmicpc.net/problem/1647

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent,parent[a])
    return parent[a]


def update_parent(parent, edge):
    a, b = edge
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a != b:
        if a<b:
            parent[b] = a
        else:
            parent[a] = b

def is_a_way(edges, a, b):
    """여기는 edges로 result가 그때그때 들어와야"""
    

# v, e = map(int, input().split())
v, e = 7, 12
edges = [] # 전체 edges
parent = [i for i in range(v+1)]
# for i in range(e):
#     a, b, cost = map(int, input().split())
#     # update_parent(parent, (a,b))
#     edges.append((cost,a,b))
edges = [(3,1,2),
        (2,1,3),
        (1,3,2),
        (2,2,5),
        (4,3,4),
        (6,7,3),
        (5,5,1),
        (2,1,6),
        (1,6,4),
        (3,6,5),
        (3,4,5),
        (4,6,7)]

edges.sort() # cost기준 오름차순 정렬됨
result = [] # 선별된 edges
final_cost = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b): # 아직 둘이 같이 묶이지 않았다면 (둘 사이를 연결하는 경로가 없다면)
        update_parent(parent, (a,b)) # 묶어주고 (뒤에 들어오는 애들은 이 둘이 연결된 걸 알 수 있게 됨)
        result.append(edge)
        final_cost += cost
        
print('최종 비용')
print(final_cost-result[-1][0]) # 가장 비용 큰 길을 빼줌 -> 두 마을로 나누기