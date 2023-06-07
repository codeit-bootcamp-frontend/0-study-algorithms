def dfs(curr, linked, visited):
    visited[curr] = True
    
    for nxt in linked[curr]:
        if not visited[nxt]:
            dfs(nxt, linked, visited)
    

def solution(n, computers):
    answer = 0
    
    linked = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    
    for x in range(n):
        for y in range(n):
            if x != y and computers[x][y] == 1:
                linked[x].append(y)
    
    for curr in range(n):
        if not visited[curr]:
            answer += 1
            dfs(curr, linked, visited)
                
    return answer
    
            