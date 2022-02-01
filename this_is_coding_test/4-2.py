n = int(input())

count = 0
for min in range(60):
    for sec in range(60):
        time = str(min)+str(sec)
        if '3' in time:
            count += 1

# count : 한 시간에 3이 등장하는 경우의 수

if n >= 3:
    print((n-n//10) * count + (60*60) * (n//10+1))
else:
    print((n+1) * count)

# 교재 풀이에서는 아예 3중 반복문으로 품
# 3이 들어있는지 확인하고 count 하는 방식은 동일