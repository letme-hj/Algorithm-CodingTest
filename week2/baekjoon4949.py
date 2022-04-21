# 균형잡힌 세상

strings = []
### 입력
while True:
    a = input()
    if a == '.':
        break

    strings.append(a)


# def balanced(s, iter):
#     print('시작 s:', s)
#     input()

#     i = s.find(r'[\(\[]')
#     print('여기서 ( 혹은 [ 를 찾았냐', i)
#     input()
#     if i == -1 and iter>0:
#         if s.find(r'[\)\]]') != -1:
#             return 'no'
#         else:
#             return 'yes'

#     if s[i]=='(':
#         print('( 을 찾았음')
#         j = s[i+1:].find(')')
        
#         if j != -1:
#             print('짝꿍 )를 찾았음')
#             s = s[:i]+s[i+1:j]+s[j+1:]
#             print('한 쌍의 () 제거한 s:',s)
#             input()
#             return balanced(s, iter+1)
#         else:
#             return 'no'
#     if s[i]=='[':
#         print('[(] 을 찾았음')

#         j = s[i+1:].find(']')
#         if j != -1:
#             print('짝꿍 ]를 찾았음')

#             s = s[:i]+s[i+1:j]+s[j+1:]
#             print('한 쌍의 [] 제거한 s:',s)
#             input()

#             return balanced(s, iter+1)
#         else:
#             return 'no'

def balanced_s(s, iter):
    print('시작 s:', s)
    input()

    i = s.find('(')
    print('여기서 ( 를 찾았냐', i)
    input()
    if i == -1:
        if s.find(')') != -1:
            return False
        else:
            return True
    else:
        # print('( 을 찾았음')
        j = s[i+1:].rfind(')')
        
        if j != -1:
            print('짝꿍 )를 찾았음', j)
            k = s[i+1:].rfind(']')
            if k>j: # 이걸 추가해서 다시 만들어보자....
                return False
            s = s[:i]+s[i+1:i+1+j]+s[i+1+j+1:]
            print('한 쌍의 () 제거한 s:',s)
            input()
            return balanced_s(s, iter+1)
        else:
            return False

def balanced_b(s, iter):
    print('시작 s:', s)
    input()

    i = s.find(r'[')
    print('여기서 [] 를 찾았냐', i)
    input()
    if i == -1:
        if s.find(r']') != -1:
            return False
        else:
            return True
    else:
        # print('] 을 찾았음')
        j = s[i+1:].find(r']')
        
        if j != -1:
            print('짝꿍 ]를 찾았음')
            s = s[:i]+s[i+1:i+1+j]+s[i+1+j+1:]
            # s = s[:i]+s[i+1:j]+s[j+1:]
            print('한 쌍의 [] 제거한 s:',s)
            input()
            return balanced_b(s, iter+1)
        else:
            return False

# 아 첫번째 뒷괄호를 기준으로 봐야겠다...
# 한문제 빼고 통과. but (()()(())) 이런 경우 못 잡음 ()() 에서 )( 로 만들어버려서..
# # def balanced(s, iter):
#     # print('시작 s:', s)
#     # input()

#     i = s.find('(')
#     j = s.find('[')
#     # print('여기서 ( 를 찾았냐', i)
#     # print('여기서 [ 를 찾았냐', j)
#     # input()
#     if i == -1 and j == -1:
#         return True

#     if i<j and i != -1:
#         m = s[i+1:].rfind(')')
#         if m != -1:
#             # print('짝꿍 )를 찾았음', m)
#             # n = s[i+1:].rfind(']')
#             # if n>m:
#             #     return False
#             if balanced(s[i+1:i+1+m], iter):

#                 s = s[:i]+s[i+1:i+1+m]+s[i+1+m+1:]
#                 # print('한 쌍의 () 제거한 s:', s)
#                 # input()
#                 return balanced(s, iter+1)
#             else:
#                 return False
#         else:
#             return False
#     elif i<j:
#         n = s[j+1:].rfind(']')
#         if n != -1:
#             # print('짝꿍 ]를 찾았음')
#             # m = s[j+1:].rfind(')')
#             # if m>n:
#             #     return False
#             if balanced(s[j+1:j+1+n], iter):
#                 s = s[:j]+s[j+1:j+1+n]+s[j+1+n+1:]
#                 # print('한 쌍의 [] 제거한 s:',s)
#                 # input()
#                 return balanced(s, iter+1)
#             else:
#                 return False
#         else:
#             return False


#     elif i>j and j!=-1:
#         n = s[j+1:].rfind(']')
#         if n != -1:
#             # print('짝꿍 ]를 찾았음')
#             # m = s[j+1:].rfind(')')
#             # if m>n:
#             #     return False
#             if balanced(s[j+1:j+1+n], iter):
#                 s = s[:j]+s[j+1:j+1+n]+s[j+1+n+1:]
#                 # print('한 쌍의 [] 제거한 s:',s)
#                 # input()
#                 return balanced(s, iter+1)
#             else:
#                 return False
#         else:
#             return False

#     elif i>j:
#         m = s[i+1:].rfind(')')
#         if m != -1:
#             # print('짝꿍 )를 찾았음', m)
#             # n = s[i+1:].rfind(']')
#             # if n>m:
#             #     return False
#             if balanced(s[i+1:i+1+m], iter):

#                 s = s[:i]+s[i+1:i+1+m]+s[i+1+m+1:]
#                 # print('한 쌍의 () 제거한 s:', s)
#                 # input()
#                 return balanced(s, iter+1)
#             else:
#                 return False
#         else:
#             return False



    # if i == -1:
    #     if s.find(')') != -1:
    #         return False
    #     else:
    #         return True
    # else:
    #     # print('( 을 찾았음')
    #     j = s[i+1:].rfind(')')
        
    #     if j != -1:
    #         print('짝꿍 )를 찾았음', j)
    #         k = s[i+1:].rfind(']')
    #         if k>j:
    #             return False
    #         s = s[:i]+s[i+1:i+1+j]+s[i+1+j+1:]
    #         print('한 쌍의 () 제거한 s:',s)
    #         input()
    #         return balanced_s(s, iter+1)
    #     else:
    #         return False

##### 다시 시도
def balanced(s, iter):
    # print('시작 s:', s)
    # input()

    i = s.find(')')
    j = s.find(']')
    # print('여기서 ( 를 찾았냐', i)
    # print('여기서 [ 를 찾았냐', j)
    # input()
    if i == -1 and j == -1:
        if s.find('[') != -1 or s.find('(') != -1:
            return False
        else:
            return True

    if i<j and i != -1:
        m = s[:i].rfind('(')
        if m != -1:
            # print('짝꿍 )를 찾았음', m)
            # n = s[i+1:].rfind(']')
            # if n>m:
            #     return False
            if balanced(s[m+1:i], iter):

                s = s[:m]+s[m+1:i]+s[i+1:]
                # print('한 쌍의 () 제거한 s:', s)
                # input()
                return balanced(s, iter+1)
            else:
                return False
        else:
            return False
    elif i<j:
        n = s[:j].rfind('[')
        if n != -1:
            # print('짝꿍 ]를 찾았음')
            # m = s[j+1:].rfind(')')
            # if m>n:
            #     return False
            if balanced(s[n+1:j], iter):
                s = s[:n]+s[n+1:j]+s[j+1:]
                # print('한 쌍의 [] 제거한 s:',s)
                # input()
                return balanced(s, iter+1)
            else:
                return False
        else:
            return False


    elif i>j and j!=-1:
        n = s[:j].rfind('[')
        if n != -1:
            # print('짝꿍 ]를 찾았음')
            # m = s[j+1:].rfind(')')
            # if m>n:
            #     return False
            if balanced(s[n+1:j], iter):
                s = s[:n]+s[n+1:j]+s[j+1:]
                # print('한 쌍의 [] 제거한 s:',s)
                # input()
                return balanced(s, iter+1)
            else:
                return False
        else:
            return False

    elif i>j:
        m = s[:i].rfind('(')
        if m != -1:
            # print('짝꿍 )를 찾았음', m)
            # n = s[i+1:].rfind(']')
            # if n>m:
            #     return False
            if balanced(s[m+1:i], iter):

                s = s[:m]+s[m+1:i]+s[i+1:]
                # print('한 쌍의 () 제거한 s:', s)
                # input()
                return balanced(s, iter+1)
            else:
                return False
        else:
            return False

result = []
for s in strings:
    print(balanced(s,0))
    input()
    if balanced(s,0):
        result.append('yes')
    else:
        result.append('no')
    # if balanced_s(s, 0) and balanced_b(s,0):
    #     result.append('yes')
    # else:
    #     result.append('no')
    # result.append(balanced(s, 0))

print(result)





####### 최종 제출


def balanced(s, iter):
    print('입력으로 받은 s:',s)

    i = s.find(')')
    j = s.find(']')
    print('여기서 ) 를 찾았냐', i)
    print('여기서 ] 를 찾았냐', j)

    if i == -1 and j == -1:
        if s.find('[') != -1 or s.find('(') != -1:
            print('), ] 는 둘다 없는데 ( 혹은 [ 가 있다?')
            return False
        else:
            return True

    # )가 ]보다 좀 앞쪽 -> ()를 먼저 보자
    if i<j and i != -1:
        m = s[:i].rfind('(') # ) 앞쪽에서 )와 가장 가까운 ( 짝꿍 찾기
        if m != -1: # 짝꿍 찾았으면
            if balanced(s[m+1:i], iter): # 그 쌍 내부도 balanced 라면
                s = s[:m]+s[m+1:i]+s[i+1:] # ( 이전 문자들 + ( 이후 ) 이전 문자들 + ) 이후 문자들 로 새로운 s 만들어 넣기
                return balanced(s, iter+1) # 그 두 쌍 제외한 문자열로 다시 확인
            else: # 그 쌍 내부가 balanced가 아니면 
                return False
        else:
            return False

    # )는 없고 ]만 있음
    elif i<j:
        n = s[:j].rfind('[') # 가장 가까운 [를 찾아야지
        if n != -1: # 있으면
            if balanced(s[n+1:j], iter): # 그 [] 내부도 균형잡혔는지 보고
                s = s[:n]+s[n+1:j]+s[j+1:] # [, ] 제외한 부분들만 가지고 다시 만들기
                return balanced(s, iter+1)
            else:
                return False
        else: # 없으면
            return False

    # )보다 ]가 먼저 있으면
    elif i>j and j!=-1:
        n = s[:j].rfind('[') # 또 가장 가까운 [ 를 찾고
        if n != -1: # 있으면
            if balanced(s[n+1:j], iter): # 그 내부도 균형잡혔는지 보고
                s = s[:n]+s[n+1:j]+s[j+1:] # 그 [, ]만 쏙 빼고 다시 만들어
                return balanced(s, iter+1) # 재귀
            else: # 없으면
                return False
        else:
            return False

    elif i>j:
        m = s[:i].rfind('(')
        if m != -1:
            if balanced(s[m+1:i], iter):
                s = s[:m]+s[m+1:i]+s[i+1:]
                return balanced(s, iter+1)
            else:
                return False
        else:
            return False

strings = []
### 입력
while True:
    a = input()
    if a == '.':
        break

    strings.append(a)

result = []
for s in strings:
    if balanced(s,0):
        # result.append('yes')
        print('yes')
    else:
        # result.append('no')
        print('no')

# print(result)  이거땜에 틀렸었네...
