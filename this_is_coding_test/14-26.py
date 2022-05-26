# 카드 정렬하기 (백준 1715)
# heapq를 많이 사용하는군/... 우선순위큐!

N = int(input())
groups = []
for i in range(N):
    groups.append(int(input()))

groups.sort(reverse=True)

sum = 0
if len(groups)==1: # 이 방식으로 할 때는 이거를 아래 while문 안에 넣으면 groups가 pop 두개 지나고 빌 때 end가 음수되는 현상...
    print(sum)
else:
    while True:

        compare = (groups.pop() + groups.pop()) # 가장 작은 개수의 묶음 두개끼리
        sum += compare

        if len(groups)==0:
            break
        
        # compare을 group에 정렬 상태 유지하면서 삽입하고픔 (이진 탐색 활용)
        start = 0
        end = len(groups)-1
        while True:
            mid = (start+end)//2
            if groups[mid] == compare:
                groups.insert(mid, compare)
                break

            if groups[mid]<compare: # compare가 더 크면 뒤쪽에서 뒤져야 함 (내림차순이니까)
                if mid==0: # mid가 0일 때는 아래 조건에서 인덱스 오류나니까 먼저 걸러줌
                    groups.insert(mid, compare)
                    break
                elif groups[mid-1]>compare: # 근데 바로 직전보다는 작다면? 뒤쪽 뒤질 필요 없이 요 자리에 들어가면 됨.
                    groups.insert(mid, compare)
                    break

                end = mid-1

            elif groups[mid]>compare: # compare가 더 작으면 앞쪽에서 뒤져야 함
                if mid == len(groups)-1: # mid가 마지막일 때는 아래 조건에서 인덱스 오류나니까 먼저 걸러줌
                    groups.insert(mid+1, compare)
                    break
                elif groups[mid+1]<compare: # 근데 바로 직후보다는 크다면? 앞쪽 뒤질 필요 없이 직후 자리로 넣어주면 됨.
                    groups.insert(mid+1, compare)
                    break
                
                start = mid + 1
                


    print(sum)


### heapq 활용
# 이진 탐색을 구현한 거 대신 heapq를 활용해 자료구조 자체가 sort되도록
import heapq
N = int(input())
groups = []
for i in range(N):
    groups.append(int(input()))

heapq.heapify(groups) # heap으로 먼저 맞춰줌

sum = 0
while True:
    if len(groups)==1:
        break

    compare = heapq.heappop(groups) + heapq.heappop(groups)
    sum += compare

    heapq.heappush(groups, compare)

print(sum)