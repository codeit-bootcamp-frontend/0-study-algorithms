# 이분 탐색
def solution(n, times):
    times.sort()
    answer = n * times[0]
    # 시작 탐색 범위: 0 ~ n * times[0]
    start = 0
    end = n * times[0]
    while start <= end:
        mid = (start + end) // 2
        # 각각의 최대 검사 인원 확인
        total_people = 0
        time_taken = 0
        for time in times:
            people = mid // time
            total_people += people
            time_taken = max(time_taken, people * time)
        # n과 비교하여 시간의 범위 결정
        if total_people < n:
            start = mid + 1
        else:
            answer = min(answer, time_taken)
            end = mid - 1

    return answer