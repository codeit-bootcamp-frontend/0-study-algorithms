import sys
limit_number = 10000
sys.setrecursionlimit(limit_number)

def solution(maps):
    answer = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    
    def dfs(x, y):
        res = int(maps[x][y])
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if next_x >= 0 and next_x < len(maps) and next_y >= 0 and next_y < len(maps[0]):
                if visited[next_x][next_y] == False and maps[next_x][next_y] != "X":
                    visited[next_x][next_y] = True
                    res += dfs(next_x, next_y)
        
        return res
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if visited[i][j] == False and maps[i][j] != "X":
                visited[i][j] = True
                size = dfs(i, j)
                if size != 0:
                    answer.append(size)
        
    if len(answer) == 0:
        return [-1]
    return sorted(answer)