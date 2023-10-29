import heapq

def solution(jobs):
    answer = 0
    jobs.sort(key=lambda x: x[0])
    q = []
    time = jobs[0][0]
    idx = 0
    length = len(jobs)
    while q or idx < length:
        # 현재 시간에 요청할 수 있는 작업 힙에 넣기
        while idx < length and jobs[idx][0] <= time:
            heapq.heappush(q, (jobs[idx][1], jobs[idx][0]))
            idx += 1
        # 나머지 작업 요청 시간이 현재 시간보다 뒤라 작업 수행이 없을 때 처리
        if idx < length and not q:
            time = jobs[idx][0]
            continue
    
        # 힙 작업 중 가장 소요시간 짧은 작업 꺼내서 수행
        next_work = heapq.heappop(q)
        next_work_during = next_work[0]
        next_work_request = next_work[1]
        answer += (time + next_work_during) - next_work_request
        time += next_work_during
    
    return answer // length