# 개미전사

N = int(input())
array = list(map(int, input().split()))
dp = [0]*N
dp[0] = array[0]

for i in range(1,N):
    print('i == ', i)
    if i == 1:
        dp[i] = max(dp[i-1], array[i])
    else:
        dp[i] = max(dp[i-1], max(dp[:i-1])+array[i])

print(dp[-1])