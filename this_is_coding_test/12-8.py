# 문자열 재정렬

S = list(input())
i = 0
int_sum = 0
num_int =0

while True:
    if i == len(S):
        break
    try:
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
if num_int >0:
    print(''.join(S)+str(int_sum))
else:
    print(''.join(S))
