from collections import deque

def solution(x, y, n):
    answer = 0
    num_set = set()
    queue = deque()
    queue.append((x, 0)) # 현재 숫자, 연산 횟수
    while queue:
        num, iter_num = queue.popleft()
        if num == y:
            return iter_num
        tri, double, plus = num * 3, num * 2, num + n
            
        if tri <= y and tri not in num_set:
            queue.append((tri, iter_num + 1))
            num_set.add(tri)
        if double <= y and double not in num_set:
            queue.append((double, iter_num + 1))
            num_set.add(double)
        if plus <= y and plus not in num_set:
            queue.append((plus, iter_num + 1))
            num_set.add(plus)

    return -1