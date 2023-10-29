def solution(n, computers):
    answer = 0
    visited = {}
    for i in range(n):
        visited[i] = False
        
    def dfs(i):
        for link_idx, is_link in enumerate(computers[i]):
            if is_link and visited[link_idx] == False:
                visited[link_idx] = True
                dfs(link_idx)

    for i in range(n):
        if visited[i] == False:
            answer += 1
            visited[i] = True
            dfs(i)
    
    return answer