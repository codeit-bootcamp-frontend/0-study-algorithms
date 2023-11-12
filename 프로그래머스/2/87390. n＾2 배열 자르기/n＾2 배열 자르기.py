def solution(n, left, right):    
    answer = []
    
    def cal_row_and_column(num):
        row = num // n
        col = num % n
        return (row, col)
    
    def cal_num_from_position(row, col):
        return max(row, col) + 1
    
    for i in range(left, right+1):
        row, col = cal_row_and_column(i)
        answer.append(cal_num_from_position(row, col))
    
    return answer