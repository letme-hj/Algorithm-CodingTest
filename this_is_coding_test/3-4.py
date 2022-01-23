n, k = map(int, input().split())
count = 0
while n != 1:
    if n % k == 0:
        n //= k
    else:
        n -= 1 # 이렇게 1씩 빼면 숫자가 매우 커졌을 때 비효율적
    count += 1
print(count)


# from here is a more efficient solution (from the book)
result = 0 # 여기서의 result는 위에서의 count에 해당 (최종 출력이 될 값)
while True:
    target = (n//k)*k
    result += (n-target)
    n = target
    if n < k:
        break
    result += 1
    n //= k

result += (n-1)
print(result)