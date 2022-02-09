n, m = map(int, input().split())
frame = []
for i in range(n):
    frame.append(list(map(int,list(input()))))

# dfs?
current = (1,1)
visited = []
def dfs(x,y, count, visited):
    if (x,y) in visited:
        return
    else:
        visited.append((x,y))

    if x<1 or x>n or y<1 or y>m:
        return
    if x==n and y==m :
        return count
    if frame[x-1][y-1] == 0:
        return
        
    if frame[x-1][y-1] == 1:
        a = dfs(x-1,y, count+1, visited)
        b = dfs(x+1,y, count+1, visited)
        c = dfs(x,y-1, count+1, visited)
        d = dfs(x,y+1, count+1, visited)
        results = [a,b,c,d]
        min = 999999999
        for i in results:
            if i is not None and i<min:
                min = i
        return min

print(dfs(1,1,1, []))