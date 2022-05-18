# 모험가길드

N = int(input()) # 1 이상  10,000 이하
scared = list(map(int, input().split()))

scared.sort(reverse=True) # sort (큰 것부터)

i = 0
count = 0
while True:
    if i >= len(scared): # index out of range 뜰 것
        break

    num_ppl = scared[i] # 그 인덱스의 공포도 (그 사람이 속할 그룹의 최소 인원 수)

    if i+num_ppl > len(scared): # 그 사람 포함해 그룹 만들 수 없으면, 공포도 더 (같거나) 작은 애로 건너뜀 (딱 알맞게 끝나는 경우 len과 같아지므로 >만)
        i = i+1
    else: # 그룹 만들어짐
        i = i+num_ppl # 다음 인덱스
        count += 1


print(count)
