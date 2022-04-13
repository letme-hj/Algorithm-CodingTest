# 삼각 달팽이



def solution(n):
    answer = [[] for _ in range(n)] # 정답 모을 것
    reverse_array = [[] for _ in range(n)] # 위쪽 방향으로 갈 때는 반대쪽에 붙어있어야 해서 따로 모으고 나중에 Reverse해서 붙일 것
    def fill(dir, range_n, start_row, start_num, array, reverse_array):
        """
        dir: 1-down, 2-right, 3-up
        """
        if dir == 1:
            # 아래로 내려갈 때
            for i in range(range_n):
                array[start_row+i].append(start_num)
                start_num += 1
            start_row = start_row + i 
        if dir == 2:
            # 오른쪽으로 갈 때
            for _ in range(range_n):
                array[start_row].append(start_num)
                start_num += 1
            start_row = start_row-1 

        if dir == 3: # 이건 각 Row에서 뒤쪽 순서부터 채워져야하니까 따로 보관! 나중에 합칠 것
            for i in range(range_n):
                reverse_array[start_row-i].append(start_num)
                start_num += 1
            start_row = start_row-i+1 


        return start_row, start_num, array, reverse_array
    
    ## 본격 코드 시작
    dir = 1
    range_n = n # 한 loop 돌 때마다 하나씩 떨어질 것
    start_row = 0 # 행
    start_num = 1 # 현재 숫자 (answer list에 추가할)

    while True:

        # stop 조건
        if range_n == 0: 
            result = []
            for i in range(len(answer)): # 행 돌면서 reversed랑 순서 맞춰 합치기
                answer[i] = answer[i]+list(reversed(reverse_array[i]))
            for i in answer: # 행 별로 나뉜 이중 리스트를 하나로 합쳐주기
                result += i
            
            answer = result
            break

        # 주요 코드
        start_row, start_num, answer, reverse_array = fill(dir, range_n, start_row, start_num, answer, reverse_array)
        range_n -= 1 # range 하나 빼줌
        if dir==3:
            dir =1
        else:
            dir += 1 # 다음 Direction으로 바꿔줌
    

    return answer

print(solution(5))