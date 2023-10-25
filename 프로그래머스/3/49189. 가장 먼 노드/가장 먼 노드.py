from collections import deque

def solution(n, edge):
    graph = {}
    visited = {}
    for i in range(1, n + 1):
        visited[i] = False
        graph[i] = []
    visited[1] = True
    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)
    
    queue = deque()
    queue.append((1, 0))
    answer = 0
    max_move = -1
    while queue:
        node, move = queue.popleft()
        if move > max_move:
            max_move = move
            answer = 1
        elif move == max_move:
            answer += 1
        
        for next_node in graph[node]:
            if visited[next_node] == False:
                visited[next_node] = True
                queue.append((next_node, move + 1))
        
    return answer