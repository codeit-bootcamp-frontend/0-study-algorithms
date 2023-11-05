def solution(scores):
    answer = 1
    wanho = scores[0]
    wanho_sum = wanho[0] + wanho[1]
    # 근무 점수 내림차순, 동료 점수 오름차순으로 정렬
    scores.sort(key=lambda x: (-x[0], x[1]))
    max_company = 0
    for score in scores:
        # 완호가 두 점수 모두 낮으면 인센티브 불가
        if wanho[0] < score[0] and wanho[1] < score[1]:
            return -1
        # max_company보다 새 점수 동료가 낮으면, 
        # 근무 점수로 내림차순 되어있기 때문에 새 점수는 인센티브에 포함될 수 없음
        if max_company <= score[1]:
            # 인센티브 포함되는 새 점수의 합과 완호 점수 합을 비교
            if wanho_sum < score[0] + score[1]:
                answer += 1
            # max_company를 갱신
            max_company = score[1]
    return answer