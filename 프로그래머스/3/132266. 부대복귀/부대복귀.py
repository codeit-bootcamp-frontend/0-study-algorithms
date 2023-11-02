from collections import deque

def solution(n, roads, sources, destination):    
    len_sources = len(sources)
    # 도착점에서 다른 노드들로의 최단 거리를 구하자
    # 그래프 및 방문 표시 만들기
    graph = {}
    visited = []
    min_distance_map = []
    for i in range(n):
        graph[i+1] = []
        visited.append(False)
        min_distance_map.append(-1)
    for road in roads:
        for i in range(2):
            graph[road[1-i]].append(road[i])

    # BFS 초기 설정
    queue = deque()
    queue.append((destination, 0))
    visited[destination-1] = True
    # BFS 순회
    while queue:
        pos, move = queue.popleft()
        if min_distance_map[pos-1] == -1:
            min_distance_map[pos-1] = move
        else:
            min_distance_map[pos-1] = min(min_distance_map[pos-1], move)
        for next_pos in graph[pos]:
            if not visited[next_pos-1]:
                queue.append((next_pos, move+1))
                visited[next_pos-1] = True
    
    # destination에서 각 source로의 최단 거리
    answer = []
    for i in range(len_sources):
        answer.append(min_distance_map[sources[i]-1])
    
    return answer