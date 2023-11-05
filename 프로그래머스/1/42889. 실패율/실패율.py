def solution(N, stages):
    challenger = [0 for _ in range(N+1)]
    failer = [0 for _ in range(N+1)]
    for stage in stages:
        if not stage == N+1:
            failer[stage-1] += 1
        for i in range(stage):
            challenger[i] += 1
    fail_rate = [[0, i+1] for i in range(N)]
    for i in range(N):
        if not challenger[i] == 0:
            fail_rate[i][0] = failer[i] / challenger[i]
    fail_rate.sort(key=lambda x: (-x[0], x[1]))
    
    answer = []
    for i in range(N):
        answer.append(fail_rate[i][1])
        
    return answer