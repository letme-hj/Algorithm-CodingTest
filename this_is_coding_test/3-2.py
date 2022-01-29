n, m, k = input().split()
n, m, k = int(n), int(m), int(k)
nums = list(map(int, input().split()))

iter = m//(k+1)
sorted_arr = sorted(nums, reverse=True)
print(sorted_arr[0] * k * iter + sorted_arr[1] * iter + sorted_arr[0] * (m%(k+1)))