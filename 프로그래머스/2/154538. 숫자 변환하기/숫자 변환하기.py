from collections import deque

def solution(x, y, n):
    answer = 0
    visited = {}
    queue = deque()
    queue.append((x, 0)) # 현재 숫자, 연산 횟수
    while queue:
        num, iter_num = queue.popleft()
        if num == y:
            return iter_num
        tri, double, plus = num * 3, num * 2, num + n
            
        if tri <= y and tri not in visited:
            queue.append((tri, iter_num + 1))
            visited[tri] = True
        if double <= y and double not in visited:
            queue.append((double, iter_num + 1))
            visited[double] = True
        if plus <= y and plus not in visited:
            queue.append((plus, iter_num + 1))
            visited[plus] = True

    return -1