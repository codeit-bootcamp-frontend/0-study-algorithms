def solution(n, s):
    if n > s:
        return [-1]
    quotient = s // n
    remainder = s % n
    
    answer = [quotient for _ in range(n)]
    idx = len(answer) - 1
    while remainder:
        answer[idx] += 1
        idx -= 1
        remainder -= 1
    
    return answer