from collections import deque

def solution(progresses, speeds):
    answer = []
    progress_queue = deque()
    speed_queue = deque()
    for progress, speed in zip(progresses, speeds):
        progress_queue.append(progress)
        speed_queue.append(speed)

    while (progress_queue):
        deploy_per_day = 0
        
        for i in range(len(speed_queue)):
            progress_queue[i] += speed_queue[i]   
            
        while progress_queue:
            if progress_queue[0] >= 100:
                progress_queue.popleft()
                speed_queue.popleft()
                deploy_per_day += 1
            else:
                break
                
        if deploy_per_day > 0:
            answer.append(deploy_per_day)
    
    return answer