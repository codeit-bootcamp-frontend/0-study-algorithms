# 플로이드 와샬 알고리즘을 유사하게 활용한다.
# 이 때 최단 거리까지 계산할 필요는 없고, 
# 거쳐가는 경로(k)가 있을 때 i -> j에 1을 넣어준다.
def solution(n, results):
    answer = 0
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for result in results:
        winner = result[0] - 1
        loser = result[1] - 1
        graph[winner][loser] = 1
        
    # k = 거쳐가는 노드
    for k in range(n):
        # i = 출발 노드
        for i in range(n):
            # j = 도착 노드
            for j in range(n):
                if not graph[i][j]:
                    if graph[i][k] and graph[k][j]:
                        graph[i][j] = 1
    rank_determined = [0 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                rank_determined[i] += 1
                rank_determined[j] += 1
    for rank in rank_determined:
        if rank == n - 1:
            answer += 1
    
    return answer