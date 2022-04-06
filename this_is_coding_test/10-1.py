# 서로소 집합 알고리즘

# ver1) 루트 노드 찾기 (속한 집합 찾기)
def find_parent(parent, x):
    if parent[x] != x: # parent 저장된 테이블에서 자기 자신이 부모가 아니라면
        return find_parent(parent, parent[x]) # 자신의 부모의 부모를 찾아가기 
                                              # (재귀적으로 부모노드를 찾아 결국 루트 노드 찾아가는 것)
    return x # 자기자신이 부모노드라면 자기자신 return

# ver2) 좀더 효율적인 루트 노드 찾기 (속한 집합 찾기) -> 부모테이블 == 속한 집합 나타내는 테이블이 됨
def find_parent2(parent, x):
    if parent[x] !=x:
        parent[x] = find_parent2(parent, parent[x])
    return parent[x]


# 연결된 노드를 하나의 집합으로 묶어주기
def union_parent(parent, a, b):
    """
    a, b는 하나의 간선으로 연결된 노드
    """
    # 각 노드의 루트 노드 찾기
    a = find_parent2(parent, a)
    b = find_parent2(parent, b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b


# -------

### [입력] 노드, 엣지 개수
v, e = map(int, input().split())


### 부모 테이블 초기화 ###
parent = [0] * (v+1) # 부모테이블 (0인 노드는 없어서? 1부터 인덱스 맞추려고 v+1개 생성
for i in range(1, v+1):
    parent[i] = i # 부모노드 자기 자신으로 초기화


### [입력] 연결된 노드들 (간선의 개수만큼 pair를 입력받게 됨)
for i in range(e):
    a, b = map(int, input().split())

    union_parent(parent, a, b) # 입력과 동시에 부모테이블 업데이트


# -------

# 각 원소가 속한 집합 출력
# print('각 원소가 속한 집합')
# for i in range(1, v+1):
#     print(find_parent(parent, i), end=' ')

print()

# 각 원소의 부모 (부모테이블) 출력
print('부모테이블')
for i in range(1, v+1):
    print(parent[i], end=' ')