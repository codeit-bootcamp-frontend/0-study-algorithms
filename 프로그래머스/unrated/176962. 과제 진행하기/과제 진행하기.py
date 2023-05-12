def getGapTime(curr_start, next_start):
    curr_start = list(map(int, curr_start.split(':')))
    next_start = list(map(int, next_start.split(':')))
    curr_minutes = curr_start[0] * 60 + curr_start[1]
    next_minutes = next_start[0] * 60 + next_start[1]
    
    return next_minutes - curr_minutes


def solution(plans):
    answer = []
    pending = []
    
    # 시작 시간 순서대로 정렬
    plans.sort(key = lambda x:x[1])
    
    for i in range(len(plans)):
        # 마지막 task는 다음 task가 없으므로 끝까지 완료
        if i == len(plans) - 1:
            answer.append(plans[i][0])
            break
        
        curr_task, curr_start, time = plans[i][0], plans[i][1], int(plans[i][2])
        next_start = plans[i+1][1]
        rest_time = getGapTime(curr_start, next_start)
        # 현재 task를 다 하지 못하면 pending에 추가
        if rest_time < time:
            pending.append((curr_task, time-rest_time))
        
        # 현재 task 이후까지 시간이 남는다면 pending에 있는 task 진행
        else:
            answer.append(curr_task)
            
            rest_time -= time
            while rest_time > 0:
                if pending:
                    pending_task, pending_task_time = pending[-1][0], pending[-1][1]
                    pending_task_time -= min(pending_task_time, rest_time)
                    # pending에 있는 task가 아직 안 끝났다면 남은 시간으로 업데이트
                    if pending_task_time > 0:
                        pending[-1] = (pending_task, pending_task_time)
                        break
                    # pending에 있는 task가 끝났다면 그 task는 pending에서 제거
                    else:
                        rest_time -= pending[-1][1]
                        answer.append(pending_task)
                        pending.pop()
                else:
                    break    
            
    # 마지막 task를 끝난 이후 pending에 아직 task가 남아 있다면
    # 차례대로 끝내기
    for task, _ in pending[::-1]:
        answer.append(task)
            
    return answer