# 떡볶이 떡 만들기

N, M = map(int, input().split())
heights = list(map(int, input().split()))

# N, M = 4, 6
# heights = [19, 15, 10, 17]

# H를 하나씩 줄여가면서 length에 H보다 큰 것들의 개수를 더하면 될 듯
H = sorted(heights)[-1]-1
length = 0
heights.sort()

start = 0
end = len(heights)

while length<M:
    mid = (start+end)//2

    if end-start <= 1:

        if heights[start]<H:
            length += len(heights[start+1:])
            H -= 1
            start, end = 0, len(heights)
        else:
            length += len(heights[start:])
            H -= 1
            start, end = 0, len(heights)
    
    elif heights[mid] == H:
        length += len(heights[mid+1:])
        H -= 1
        start, end = 0, len(heights)
    elif heights[mid] < H:
        start = mid+1
    else:
        end = mid

print(H+1)



# 이진탐색 (책 풀이)
result = 0
while(start<=end):
    total = 0
    mid = (start+end)//2 # 이걸 H로 삼을 것
    for x in heights:
        if x>mid:
            total += x-mid
    
    if total < M:
        end = mid-1
    else:
        result = mid # 이미 result에 값이 들어갔더라도 update!
        start = mid+1
