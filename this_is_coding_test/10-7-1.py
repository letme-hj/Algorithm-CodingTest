# 팀 결성

# a의 팀 확인
def find_team(team, a):
    if team[a] != a:
        team[a]= find_team(team, team[a])
    return team[a]

# 같은 팀 여부 확인
def same_team(team, a, b):
    if find_team(team,a) == find_team(team,b):
        return True
    else:
        return False

# 팁합치기
def union(team, a, b):
    if not same_team(team, a, b):
        if a<b:
            team[b] = a
        else:
            team[a] = b


n, m = map(int, input().split())
ops = [union, same_team] # 어차피 출력이 달라서 if문으로 나누기 땜에 굳이 인덱싱해서 함수 사용할 필요없음,,,
team = [i for i in range(n+1)]

for i in range(m):
    op, a, b = map(int, input().split())
    if op==1:
        true = ops[op](team, a, b)
        if true:
            print('YES') # 한번에 출력해야하면 리스트에 보관해두고 for문 다 돈 다음에 출력하기
        else:
            print('NO')
    else:
        ops[op](team,a,b)
    
