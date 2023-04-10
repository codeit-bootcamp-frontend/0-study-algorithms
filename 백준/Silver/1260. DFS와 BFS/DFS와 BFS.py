# 실버2

def dfs(V):
    visited[V] = 1
    print(V, end=" ")
    for i in range(1, N+1):
        if not visited[i] and (graph[V][i] or graph[i][V]):
            dfs(i)


def bfs(V):
    queue.append(V)
    visited2[V] = 1
    while queue:
        V = queue.pop(0)
        print(V, end=" ")
        for i in range(1, N+1):
            if not visited2[i] and (graph[V][i] or graph[i][V]):
                queue.append(i)
                visited2[i] = 1
    #


N, M, V = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)
visited2 = [False] * (N + 1)
queue = []
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

dfs(V)
print()
bfs(V)
