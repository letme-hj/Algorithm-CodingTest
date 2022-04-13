# 삼각 달팽이



def solution(n):
    answer = [[] for _ in range(n)]
    reverse_array = [[] for _ in range(n)]
    def fill(dir, range_n, start_row, start_num, array, reverse_array):
        """
        dir: 1-down, 2-right, 3-up
        """
        if dir == 1:
            for i in range(range_n):
                array[start_row+i].append(start_num)
                start_num += 1
            start_row = start_row + i 
        if dir == 2:
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
    
    dir = 1
    range_n = n
    start_row = 0
    start_num = 1

    while True:
        if range_n == 0:
            result = []
            for i in range(len(answer)):
                answer[i] = answer[i]+list(reversed(reverse_array[i]))
            for i in answer:
                result += i
            
            answer = result
            break
        start_row, start_num, answer, reverse_array = fill(dir, range_n, start_row, start_num, answer, reverse_array)
        range_n -= 1
        if dir==3:
            dir =1
        else:
            dir += 1
    

    return answer

print(solution(5))