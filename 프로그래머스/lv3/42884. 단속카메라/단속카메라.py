def solution(routes):
    answer = 0
    
    routes.sort(key=lambda x: x[1])
    
    i = 0
    while i < len(routes):
        answer += 1
        camera_position = routes[i][1]
        
        for nxt in range(i+1, len(routes)):
            start, end = routes[nxt][0], routes[nxt][1]
            if start <= camera_position <= end:
                i += 1
            else:
                break
        i += 1
        
    return answer
        
        
        