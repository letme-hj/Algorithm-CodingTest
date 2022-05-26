# 주몽
# 한 번 사용한 재료는 다른 재료와 사용될 수 없는 거겠지?

N = int(input())
M = int(input())

ingredients = list(map(int, input().split())) # len(ingredients) = N
ingredients.sort()

left = 0
right = N-1
count = 0

while True:
    if left >= right:
        break
    num_sum = ingredients[left] + ingredients[right]

    if num_sum == M:
        left += 1
        right -= 1
        count += 1

    elif num_sum < M:
        left += 1

    else:
        right -= 1
        
print(count)