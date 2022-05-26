# 특정 거리의 도시 찾기 (백준 18352)


# N: 도시 개수, M: 도로 개수, K: (최단)거리 정보, X: 출발 도시 번호
N, M, K, X = map(int, input().split()) 

graph = [[] for _ in range(N+1)] # 도시 인덱스: 0 ~ N-1
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    # graph.append(list(map(int,input().split())))

visited = {X} # ***

dist = 0
current_city = [X]
result = None


while True:
    
    dist += 1

    # 지금 갈 수 있는 바로 다음 스텝 도시들 집합
    next_cities = set(sum([graph[i] for i in current_city], []))

    # dist==K 면 이 도시들을 출력해야 함.
    if dist == K:
        result = []
        for city in next_cities:
            if city not in visited: # 이미 방문했다면 K가 최소 거리가 아니므로!! 방문 안된 경우만 Result에 저장
                result.append(city)
        if result == []: # dist=K일 때 방문할 수 있는 city 없으면 -1 출력
            result.append(-1)
        break

    else:
        visited = visited.union(next_cities)

    current_city = next_cities

for i in sorted(result):
    print(i)

