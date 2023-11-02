import heapq

def solution(N, road, K):
    # 다익스트라 알고리즘 연습
    INF = 1e8
    
    # 그래프, 거리 리스트 생성
    graph = [[] for _ in range(N+1)]
    for vertex in road:
        s, e, w = vertex
        graph[s].append((e, w))
        graph[e].append((s, w))
    distance = [INF] * (N+1)
    distance[1] = 0
    
    # 힙 초기화
    queue = []
    heapq.heappush(queue, (1, 0)) # 출발지, 거리
    # 힙 순회
    while queue:
        cur_node, cur_w = heapq.heappop(queue)
        # 이미 최단 거리가 가중치보다 작으면 생략
        if distance[cur_node] < cur_w:
            continue
        # 다음 노드 경유
        for next_node, added_w in graph[cur_node]:
            next_w = cur_w + added_w
            # 경유해서 가는 거리가 더 짧으면 distance 경신
            if next_w < distance[next_node]:
                distance[next_node] = next_w
                heapq.heappush(queue, (next_node, next_w))
    
    # 최단 거리가 K 이하인 노드 개수
    answer = 0
    for d in distance:
        if d <= K:
            answer += 1
    return answer