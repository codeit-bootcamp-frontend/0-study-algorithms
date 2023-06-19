import heapq

def solution(N, road, K):
    linked = {}
    visited = [False for _ in range(N+1)]
    for s, e, d in road:
        if s in linked:
            linked[s].append((d, e))
        else:
            linked[s] = [(d, e)]
            
        if e in linked:
            linked[e].append((d, s))
        else: 
            linked[e] = [(d, s)]
            
    candidates = [(0, 1)]
    answer = 0
    while candidates:
        dist, point = heapq.heappop(candidates)
        
        # 현재 구한 최소 거리가 K 초과라면 탐색을 종료한다. 
        if dist > K:
            break
            
        if not visited[point]:
            answer += 1
            visited[point] = True
            
            # 현재 갈 수 있는 포인트들을 candidates에 추가
            for d, np in linked[point]:
                if not visited[np]:
                    heapq.heappush(candidates, (dist + d, np))
                
    return answer
            
            
    
    