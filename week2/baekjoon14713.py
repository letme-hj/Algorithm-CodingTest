# 앵무새

# 앵무새 n마리 이용해 전달할 것
# 앵무새 한마리당 한 문장 기억. 단어들 순서로 말함
# 다음 단어 말하기 전 인터셉 가능
# 단어 말하는 도중에는 말 가로채지 않음
# 모든 단어는 한번씩만 등장. 전체 앵무새 합쳐서도.

# 입력
N = int(input())
sentences = []
for i in range(N):
    sentences.append(input().split())

Q = input().split()

# 맨 앞 단어만 저장
candidates = [sent[0] for sent in sentences]

def update_candidates(sent_idx, sentences, candidates):

    sentences[sent_idx] = sentences[sent_idx][1:]

    if len(sentences[sent_idx])==0:
        candidates[sent_idx] = -1 # 그 sent 이제 비었으면 candidate에 -1 채워주기
    else:
        candidates[sent_idx] = sentences[sent_idx][0]
    return sentences, candidates

found = None
for word in Q:
    found = False

    for i in range(len(candidates)):
        if word == candidates[i]:
            sentences, candidates = update_candidates(i, sentences, candidates)
            found = True
            break
        
    if not found:
        print('Impossible')
        break

if sum([type(i)==int for i in candidates]) == N and found: # 이것이 중요했다,,,,
    print('Possible')
elif found:
    print('Impossible')
