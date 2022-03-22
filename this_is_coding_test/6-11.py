# 성적 낮은 순서로 학생 출력하기

N = int(input())
students = []
for i in range(N):
    students.append(input().split())

students = list(map(lambda x: [x[0], int(x[1])], students))

idx = list(zip(list(range(N)), [x[1] for x in students])) # 이 과정 필요 없음..
order = sorted(idx, key=lambda x: x[1])
student_order = [students[i[0]][0] for i in order] 

print(student_order)