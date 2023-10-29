def solution(routes):
    answer = 0
    last_search_pos = -30001
    routes.sort(key=lambda x: x[1])
    
    for route in routes:
        if last_search_pos < route[0]:
            answer += 1
            last_search_pos = route[1]
    
    return answer