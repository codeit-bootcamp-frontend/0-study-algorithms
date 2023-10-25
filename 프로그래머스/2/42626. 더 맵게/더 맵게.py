import heapq

def solution(scoville, K):
    answer = 0
    q = []
    if min(scoville) >= K:
        return answer
    for i in scoville:
        heapq.heappush(q, i)
    while len(q) >= 2:
        min_1 = heapq.heappop(q)
        if min_1 >= K:
            return answer
        answer += 1
        min_2 = heapq.heappop(q)
        new_v = min_1 + min_2*2
        heapq.heappush(q, new_v)
    if heapq.heappop(q) >= K:
        return answer
    return -1