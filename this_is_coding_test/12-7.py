# 럭키스트레이트

N = list(input())
N = list(map(int, N))

# if len(N)%2 == 1:
#     print('READY')

split1 = N[:len(N)//2]
split2 = N[len(N)//2:]

if len(N)%2==0 and sum(split1) == sum(split2):
    print('LUCKY')
else:
    print('READY')