# 바닥공사

N = int(input())

dp = [1]

for i in range(1,N+1):
    if i ==1:
        dp.append(1)
    else:
        dp.append(dp[i-1] + dp[i-2]*2)
        

print(dp[N]%796796)
    
