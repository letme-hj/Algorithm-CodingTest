# 문자열 재정렬

S = list(input())
i = 0 # 문자 하나하나 의미하는 인덱스
int_sum = 0 # 정수 합
num_int = 0 # 정수 개수 (0개일 땐 int_sum 0을 내보내면 안되므로)

while True:
    if i == len(S):
        break
    try: # 정수로 변환이 안되면 except로 넘어갈 것 (넘어가면 다음 인덱스)
        int_sum += int(S[i])
        num_int += 1
        del S[i] # 지워줄 때는 i가 다음 숫자로 넘어가면 안되므로 while로 i를 조절할 수 있게 함,,
    except:
        i+=1

# for i in range(len(S)):
#     try:
#         # print(S[i])
#         # print(int(S[i]))
#         int_sum += int(S[i])
#         num_int += 1
#         del S[i]
#     except:
        
#         print(S[i])
#         # print(int(S[i]))
#         input()

S.sort()
if num_int > 0:
    print(''.join(S)+str(int_sum))
else:
    print(''.join(S))
