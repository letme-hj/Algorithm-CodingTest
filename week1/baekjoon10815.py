# 숫자 카드

##### [1번째 시도]
##### 시간 초과 : in 때문인가? 효율적인 내장함수 아닌가..?
##### list - in은 잘 안쓰나...? set으로 바꿔서하니까 작동하네,,

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))

result = []

for i in find:
    if i in nums:
        result.append(1)
    else:
        result.append(0)

for i in result:
    print(i, end=' ')


##### [2번째 시도]
##### 이진탐색

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))

# 오름차순 정렬
nums.sort()

for i in find:
    start = 0
    end = len(nums)-1
    found=False

    while start<=end:
        mid = int((start+end)/2)
        if nums[mid]==i:
            print(1, end=' ')
            found=True
            break
        elif nums[mid]<i:
            start=mid+1
        else:
            end=mid-1
    
    if not found:
        print(0, end=' ')

##### [3번째 시도]
##### 그때그때 print하지 말고 처음처럼 result에 모아서 프린트!
n = int(input())
nums = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))

# 오름차순 정렬
nums.sort()
result=[]

for i in find:
    start = 0
    end = len(nums)-1
    found=False

    while start<=end:
        mid = int((start+end)/2)
        if nums[mid]==i:
            result.append('1')
            found=True
            break
        elif nums[mid]<i:
            start=mid+1
        else:
            end=mid-1
    
    if not found:
        result.append('0')

print(' '.join(result))


##### [4번째 시도]
##### 첫번째 시도 set으로 바꾸고 result에 모아서 출력하는 방식으로

n = int(input())
nums = set(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))

result = []

for i in find:
    if i in nums:
        result.append('1')
    else:
        result.append('0')

print(' '.join(result))


##### [5번째 시도]
##### 4번째랑 같은데 int 대신 str으로 그대로 (int 변환 아무것도 없이)

n = input()
nums = set(input().split())
m = input()
find = input().split()

result = []

for i in find:
    if i in nums:
        result.append('1')
    else:
        result.append('0')

print(' '.join(result))