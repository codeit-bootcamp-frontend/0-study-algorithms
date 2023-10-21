from collections import deque

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    queue = deque()
    queue.append((1, 0, 0))
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[False for _ in range(M)] for _ in range(N)]
    
    while queue:
        move_num, curr_x, curr_y = queue.popleft()
        # 도착점 확인
        if curr_x == N - 1 and curr_y == M - 1:
            return move_num
        
        # 다음칸 이동
        for i in range(4):
            next_x = curr_x + dx[i]
            next_y = curr_y + dy[i]
            if next_x >= 0 and next_x < N and next_y >= 0 and next_y < M:
                if maps[next_x][next_y] == 1 and visited[next_x][next_y] == False:
                    queue.append((move_num + 1, next_x, next_y))
                    visited[next_x][next_y] = True
            
    return -1