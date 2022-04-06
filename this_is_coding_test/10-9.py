# 커리큘럼

n = int(input())

times = [0 for i in range(n+1)] # 과목별 시간
pre = [[] for i in range(n+1)] # 과목별 선수과목 번호 모음

### 입력
for i in range(1, n+1): # 0은 버리는 인덱스
    lecture = list(map(int, input().split()))
    times[i] = lecture[0]
    pre[i] += lecture[1:-1]

total_time = [times[i] for i in range(n+1)] # 결과 저장할 리스트 (선수강의 없는 애부터 채울 것)
n_pre = [len(pre[i]) for i in range(n+1)] # 과목별 선수과목 개수
n_pre = sorted(list(set(n_pre[1:]))) # 과목별 선수과목 개수 unique한 값들만 모음 (돌면서 작은 개수인 애들부터 total_time 채울 것)

for num in n_pre: # 선수과목 없는 순으로!
    for pre_i in range(1,n+1): # 모든 과목을 돌면서
        if len(pre[pre_i])==num: # 선수 과목의 개수가 num인 과목을 찾아서
            max_time = 0 # 선수과목들 다 듣는 데에 걸리는 최소 시간 (초기화)
            if num!=0: # 선수과목이 없으면 그냥 max_time = 0으로 유지
                max_time = max([total_time[i] for i in pre[pre_i]]) # 선수과목 있으면 현재 저장된 선수과목 듣기까지의 시간 중 제일 오래걸리는 애 고르기
                                                                    # 그게 곧 전체 선수과목 듣는 데에 걸리는 시간 (동시에 들을 수 있으니)
            total_time[pre_i] = max_time + times[pre_i] # 선수과목 듣는 데에 걸리는 시간 + 이 과목 들을 때 걸리는 시간 으로 Total_time 해당 인덱스 업데이트

for i in range(1, n+1):
    print(total_time[i])
