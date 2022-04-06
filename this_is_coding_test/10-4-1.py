# 서로소 집합을 활용한 사이클 판별 (무방향 그래프 ONLY)

###### 서로소 집합 알고리즘에서 가져온 함수... #####
# 그래프를 가지고 -> 집합 개념으로 가져가는 함수들이 아래 두 함수.
# 단순히 연결된 부모 노드 찾는 거랑 느낌 다름. "속한 집합" 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
############################################

# [입력] 노드/간선 개수
v, e = map(int, input().split())


# 부모테이블 초기화
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i


# cycle
cycle=False

for i in range(e):
    # [입력] 간선 정보 (연결된 노드 정보)
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle=True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print('사이클 발생')
else:
    print('NO 사이클')