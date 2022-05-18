# 곱하기 혹은 더하기

S = list(input()) # 1 <= len(S) <= 20
S = list(map(int, S))

# result 초기화
result = S[0]

for i in range(1, len(S)):
    if result+S[i] >= result*S[i]:
        result = result+S[i]
    else:
        result = result*S[i]

print(result)
