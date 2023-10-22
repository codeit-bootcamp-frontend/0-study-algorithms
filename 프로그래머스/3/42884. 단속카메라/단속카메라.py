def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[0])
    idx = 0
    
    while idx < len(routes) - 1:
        answer += 1
        start = routes[idx][0]
        end = routes[idx][1]
        search = start
        while search <= end:
            while idx < len(routes) - 1 and routes[idx + 1][0] <= search:
                end = min(end, routes[idx + 1][1])
                idx += 1
            search += 1
        idx += 1
        
    if idx == len(routes) - 1:
        answer += 1
    
    return answer