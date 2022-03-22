# 두 배열의 원소 교체

N, K = list(map(int, input().split()))

A = list(map(int, input().split()))
B = list(map(int, input().split()))

a_sorted = sorted(A)
b_sorted = sorted(B)

for _ in range(K):
    if a_sorted[0] < b_sorted[-1]:
        a_sorted[0], b_sorted[-1] = b_sorted[-1], a_sorted[0]
    
    a_sorted.sort()
    b_sorted.sort()

print(sum(a_sorted))
