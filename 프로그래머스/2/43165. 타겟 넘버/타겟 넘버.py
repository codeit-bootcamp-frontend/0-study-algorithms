from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append((0, 0))
    
    while queue:
        pos, curr_sum = queue.popleft()
        next_plus = curr_sum + numbers[pos]
        next_minus = curr_sum - numbers[pos]
        
        if pos == len(numbers) - 1:
            if next_plus == target:
                answer += 1
            if next_minus == target:
                answer += 1
        else:
            queue.append((pos+1, next_plus))
            queue.append((pos+1, next_minus))
    
    return answer