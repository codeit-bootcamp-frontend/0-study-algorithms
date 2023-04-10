# 실버 3
# 25분 추천
# 딕셔너리 사용?
from collections import deque
test_case = int(input())
for t in range(test_case):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    queue = deque((data, i) for i, data in enumerate(queue))
    count = 0

    while True:
        if queue[0][0] < max(queue, key=lambda x: x[0])[0]:
            queue.rotate(-1)
        else:
            answer = queue.popleft()
            count += 1
            if answer[1] == M:
                print(count)
                break

