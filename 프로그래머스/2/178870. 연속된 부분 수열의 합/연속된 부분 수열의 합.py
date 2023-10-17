def solution(sequence, k):
    answer = []
    left, right = 0, 0
    sum_check = sequence[left]
    length = len(sequence)
    while (right < length and left <= right):
        # 합이 일치할 때
        if sum_check == k:
            if len(answer) == 0:
                answer = [left, right]
            else:
                if (answer[1] - answer[0]) > (right - left):
                    answer = [left, right]

        # 다음 연산 준비
        if sum_check <= k:
            right += 1
            # 오른쪽 도달 확인
            if right < length:
                sum_check += sequence[right]
        else:
            sum_check -= sequence[left]
            left += 1

    return answer