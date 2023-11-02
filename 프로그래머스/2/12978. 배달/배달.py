import heapq

def solution(N, road, K):
    # 다익스트라 알고리즘 연습
    # 우선순위 큐는 데이터의 첫 번째 요소의 최솟값을 기준점으로 잡는다.
    # 따라서 우선순위 큐에서 가장 가까운 노드를 꺼내기 위해 (가중치, 노드)의 순서로 되어있는 데이터를 만들어 넣어줘야 한다.
    INF = 1e8
    
    # 그래프, 거리 리스트 생성
    graph = [[] for _ in range(N+1)]
    for vertex in road:
        s, e, w = vertex
        graph[s].append((e, w))
        graph[e].append((s, w))
    distance = [INF] * (N+1)
    
    # 힙 초기화
    queue = []
    heapq.heappush(queue, (0, 1)) # 가중치, 출발지
    distance[1] = 0
    # 힙 순회
    while queue:
        # 우선순위 큐를 사용해서 cur_w가 가장 작은 노드가 먼저 나온다.
        cur_w, cur_node = heapq.heappop(queue)
        # 이미 최단 거리가 가중치보다 작으면(=이미 방문한 셈) 생략
        if distance[cur_node] < cur_w:
            continue
        # 다음 노드 경유
        for next_node, added_w in graph[cur_node]:
            next_w = cur_w + added_w
            # 경유해서 가는 거리가 더 짧으면 distance 경신
            if next_w < distance[next_node]:
                distance[next_node] = next_w
                heapq.heappush(queue, (next_w, next_node))
    
    # 최단 거리가 K 이하인 노드 개수
    answer = 0
    for d in distance:
        if d <= K:
            answer += 1
    return answer