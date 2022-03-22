# 부품 찾기

from dataclasses import dataclass
import sys

N = int(input())
db = list(map(int, input().split()))
M = int(input())
client = list(map(int, input().split()))

yes = []

# 파이썬 라이브러리 사용
for i in client:
    if i in db:
        yes.append('yes')
    else:
        yes.append('no')


# 이진트리
# db = sorted(db) # 일단 정렬
start = 0
end = len(db)
now = (start+end)//2

def binary_search(key, array):
    if len(array) == 0:
        return 'no'
    start = 0
    end = len(array)-1
    now = (start+end)//2
    if key == array[now]:
        return 'yes'
    elif key > now:
        start = now+1
        return binary_search(key, array[start:])
    elif key < now:
        end = now
        return binary_search(key, array[:end])
        
for i in client:
    yes.append(binary_search(i, db))


# print(yes)


# # 계수탐색
n = int(input())

counts = [0]*1000001
yes = []

for i in input().split():
    counts[int(i)] += 1

m = int(input())

for key in input().split():
    if counts[int(key)] != 0:
        yes.append('yes')
    else:
        yes.append('no')

# print(yes)
