### [1번째 시도] 과자 나눠주기

import numpy as np
import copy

m, n = map(int, input().split())
l = list(map(int, input().split()))

assert len(l)==n

l = np.array(l)

def how_many(length, l):
    """
    length 길이의 과자는 몇 개 만들 수 있는가!
    """
    total=0
    # list는 이렇게 안하면 아래 길이 줄이는 거에서 inplace로 계속 리스트가 업데이트돼버림
    l = copy.deepcopy(l) 

    while True:
        if sum(length<=l)<1:
            return total
        else:
            total += sum(length<=l)
            l-= length
        
start = 0
end = max(l)
optimal_l = 0

while True:
    mid = (start+end)//2

    print('길이', mid)
    print('몇개 줄 수 있어?', how_many(mid, l))
    if start>end:
        print('다 끝났어 빠빠이')
        break

    if how_many(mid, l)>=m:
        print(f'{m}명 충분히 줄 수 있어 더 큰건 없나?')
        input()
        if optimal_l < mid:
            optimal_l = mid
        start = mid+1 # 더 큰것도 되는지는 보자
    
    elif how_many(mid, l)<m:
        print(f'{m}명 다 못줘 길이 좀 줄이자')
        input()
        end = mid-1
        


print(optimal_l)


### [2번째 시도] numpy 제거(?)

import copy

m, n = map(int, input().split())
l = list(map(int, input().split()))

assert len(l)==n

def how_many(length, l):
    """
    length 길이의 과자는 몇 개 만들 수 있는가!
    """
    total=0
    # list는 이렇게 안하면 아래 길이 줄이는 거에서 inplace로 계속 리스트가 업데이트돼버림
    l = copy.deepcopy(l)
    for i in l:
        if i >= length:
            total += i//length
    return total

    # while True:
    #     # how_many_left = sum([length<=i for i in l])
    #     how_many_left = len(l)
    #     if how_many_left<1:
    #         return total
    #     else:
    #         total += how_many_left
    #         l = [i-length for i in l if length<=i]
        
start = 0
end = max(l)
optimal_l = 0

while True:
    mid = (start+end)//2

    if start>end or mid ==0:
        break

    if how_many(mid, l)>=m:
        if optimal_l < mid:
            optimal_l = mid
        start = mid+1 # 더 큰것도 되는지는 보자
    
    elif how_many(mid, l)<m:
        end = mid-1
        


print(optimal_l)


##### [3번째 시도] 최종 제출 코드 #####
m, n = map(int, input().split())
l = list(map(int, input().split()))

def how_many(length, l):
    total=0
    for i in l:
        if i>=length:
            total += i//length
    return total
        
start = 0
end = max(l)
optimal_l = 0

while True:
    mid = (start+end)//2

    if start>end or mid ==0:
        break

    if how_many(mid, l)>=m:
        if optimal_l < mid:
            optimal_l = mid
        start = mid+1
    
    elif how_many(mid, l)<m:
        end = mid-1
        

print(optimal_l)


## [4번째 시도] 추가 제출 (함수 없애고 코드 안에 직접 연산)->메모리/시간 다 줄어들었음
m, n = map(int, input().split())
l = list(map(int, input().split()))

start = 0
end = max(l)
optimal_l = 0

while True:
    mid = (start+end)//2

    if start>end or mid ==0:
        break
    
    total = 0
    for i in l:
        if i >= mid:
            total += i//mid

    if total>=m:
        if optimal_l < mid:
            optimal_l = mid
        start = mid+1
    
    elif total<m:
        end = mid-1
        

print(optimal_l)

## [5번째 시도] 추가 제출 (입력을 sys.stdin으로 받고, // 대신 int(연산결과) 사용)-> 후자가 시간을 대폭 줄여줌..!

import sys

m, n=map(int, sys.stdin.readline().split())
l=list(map(int, sys.stdin.readline().split()))

start = 1
end = max(l)
optimal_l = 0

while True:
    mid = int((start+end)/2)

    if start>end:
        break

    total = 0
    for i in l:
        if i >= mid:
            total += i//mid

    if total>=m:
        if optimal_l < mid:
            optimal_l = mid
        start = mid+1
    
    elif total<m:
        end = mid-1
        

print(optimal_l)