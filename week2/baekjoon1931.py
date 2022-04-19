# 회의실 배정
# 한개의 회의실에 가장 회의를 많이 할 수 있는 개수
# 모든 회의가 포함되어야 할 필요는 없는 듯

# 끝나는 시각 기준으로 정렬

import heapq

n = int(input()) # >= 1
meeting = []
for i in range(n):
    s, e = map(int, input().split()) # 시작 시간, 끝나는 시간 >=0 정수
    meeting.append((e,s)) # 끝나는 시간 짧은 순으로 볼 것


# 회의가 끝날때마다 가장 회의시간 짧은 애를 가져와

meeting.sort(key=lambda x: x[1]) # 우선 둘 째 원소(starT) 기준 정렬, heapq로 일찍 끝나는거부터 가져올 것
heapq.heapify(meeting)

m = heapq.heappop(meeting)
# print('1번째:', m)
e = m[0]
s = m[1]
# meeting = meeting[1:] # heappop 때문에 이미 제거되었을 것
count = 1

while True:
    found=False
    if len(meeting)==0:
        # print(len(meeting))
        break

    while True:
        m = heapq.heappop(meeting)
        # print('현재 보고 있는 회의', m)
        # print('meeting', meeting)
        # input()
        if m[1]>=e:
            # print('다음 미팅 찾았다')
            # print(m)
            # input()
            s = m[1]
            e = m[0]
            found = True
            count += 1
            break
    if not found:
        break 
    

print(count)

#     for i in range(len(meeting)):
#         m = meeting[i]
#         if m[1]>=e:
#             s = m[1]
#             e = m[0]
#             meeting = meeting[i+1:] # 이러면 i가 마지막 원소였던 경우 문제 생기는데...
#             found=True
#             count+=1
#             break

#     if not found:
#         break

#     if len(meeting) ==0:
#         break

# print(count)
