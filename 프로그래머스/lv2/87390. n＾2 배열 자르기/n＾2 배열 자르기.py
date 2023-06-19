def solution(n, left, right):
    answer = []
    for curr in range(left, right+1):
        col = curr // n
        row = curr % n
        
        answer.append(max(col, row) + 1)
        
    return answer