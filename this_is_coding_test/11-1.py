# 모험가길드

N = int(input()) # 1 이상 10,000 이하
scared = list(map(int, input().split()))

# scared.sort(reverse=True) # sort (큰 것부터)

# i = 0
# count = 0
# while True:
#     if i >= len(scared): # index out of range 뜰 것
#         break

#     num_ppl = scared[i] # 그 인덱스의 공포도 (그 사람이 속할 그룹의 최소 인원 수)

#     if i+num_ppl > len(scared): # 그 사람 포함해 그룹 만들 수 없으면, 공포도 더 (같거나) 작은 애로 건너뜀 (딱 알맞게 끝나는 경우 len과 같아지므로 >만)
#         i = i+1
#     else: # 그룹 만들어짐
#         i = i+num_ppl # 다음 인덱스
#         count += 1


# print(count)


# 위의 풀이는 틀린 듯... 633333321 ...

# 5
# 5 5 5 5 5

# 5
# 1 1 1 1 1

# 123333336
# 작은 순서로 sort하고 가야할 듯

scared.sort()
i = 0
count = 0
num_ppl = scared[0] # 초기화

while True:
    if i>=len(scared) or i+num_ppl-1>=len(scared): # index 오류가 나도록 i/num_ppl이 커지면 break

        break

    if scared[i+num_ppl-1] <= num_ppl: # i의 공포도만큼 사람 채웠을 때 그 사람의 공포도가 i이하이면
        print(i)
        print('count +')
        input()
        count += 1 # 그렇게 그룹 하나 만들면 됨

        # 인덱스 업데이트해주고(온 만큼)
        i += num_ppl 
        num_ppl = scared[i]
    
    else: # 근데 (최소)공포도만큼 사람 채웠더니 그 마지막 사람은 공포도가 더 높다면? -> 사람 더 채워야됨
        print(i)
        print('else')
        input()
        # num_ppl = scared[i]
        # if i+num_ppl-1 >= len(scared)
        if i+num_ppl-1 >= len(scared):
            break

        num_ppl = scared[i+num_ppl-1] # 마지막 원소의 공포도를 num_ppl로 업데이트해줌 
                                    # 인덱스는 변함 없기 때문에 while문 처음으로 돌아가면서 최소 공포도가 업데이트되는 늑김


print(count)
