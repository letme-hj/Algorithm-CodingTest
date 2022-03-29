# 효율적인 화폐 구성

N, M = list(map(int, input().split()))
types = []
for i in range(N):
    types.append(int(input()))

types.sort(reverse=True)
count = 1
stop = 0 # stopping 
price = types.copy()

if M in types:
    print(count)

count = 2

while True:
    # print('price len:', l)
    # print('price:', price)
    # print('몇 개로 만드는 거 확인 중?', count)
    new_price = []
    for i in price:

        for j in types:
            # print('i:', i, '| j:', j)
            # input()
            if M == i+j:
                print(count)
                stop = 1
                break
            else:
                new_price.append(i+j)
        if stop == 1:
            break
    count+=1
    price = list(set(new_price))
    for i in range(len(price)):
        if price[i] < M:
            continue
        if i == len(price)-1:
            print(-1)
            stop = 1
    # print('새로운 price list:', price)
    
    if stop == 1:
        break
