result = 0

import time
lst = list(range(100000))
start = time.time()
for i in lst:
    result += i

end = time.time()

print('for문 실행 시간:', end-start)

start = time.time()
sum(lst)
end = time.time()
print('sum 실행 시간:', end-start) # 10배 정도 빠른듯,,?!