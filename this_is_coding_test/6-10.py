# 위에서 아래로

N = int(input())
array = []
for i in range(N):
    array.append(int(input()))

print(list(reversed(sorted(array)))) # or sorted(array, reverse=True)