from collections import deque

def solution(priorities, location):
    queue = deque()
    answer = 0
    for i in range(len(priorities)):
        queue.append((i, priorities[i]))
    order = 1
    while queue:
        temp_idx = 0
        for i in range(1, len(queue)):
            if queue[i][1] > queue[temp_idx][1]:
                temp_idx = i
                
        for _ in range(temp_idx):
            queue.append(queue.popleft())
        if queue.popleft()[0] == location:
            return order
    
        order += 1
    
    return answer