def isInRange(currX, currY, x1, y1, x2, y2, direction):
    if direction == 0:
        return currY <= y2-1
    elif direction == 1:
        return currX <= x2-1
    elif direction == 2:
        return currY >= y1-1
    elif direction == 3:
        return currX >= x1-1


def solution(rows, columns, queries):
    answer = []
    
    rc = []
    for i in range(rows):
        rc.append([(i*columns) + (c+1) for c in range(columns)])
        
    for query in queries:
        x1, y1, x2, y2 = query
        
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        direction = 0
        curr_x, curr_y = x1-1, y1-1
        
        curr_target, next_target = rc[curr_x][curr_y], rc[curr_x][curr_y]
        min_num = curr_target
        while(True):
            if direction == 3 and curr_x == x1-1 and curr_y == y1-1:
                answer.append(min_num)
                break
                
            curr_target = next_target
            nx, ny = curr_x + dx[direction], curr_y + dy[direction]
            if not isInRange(nx, ny, x1, y1, x2, y2, direction):
                direction += 1
                nx, ny = curr_x + dx[direction], curr_y + dy[direction]
            next_target = rc[nx][ny]
            min_num = min(min_num, next_target)
            
            # 한 칸 이동
            rc[nx][ny] = curr_target
            curr_x, curr_y = nx, ny
            
    return answer