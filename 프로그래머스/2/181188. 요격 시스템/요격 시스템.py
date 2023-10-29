def solution(targets):
    answer = 0
    targets.sort(key=lambda x: (x[1], -x[0]))
    end_point = -1
    for target in targets:
        if end_point <= target[0]:
            answer += 1
            end_point = target[1]
        
    return answer