def solution(sequence, k):
    answer = []
    
    # 투 포인터
    left, right = 0, 0
    
    min_length = 1000001  # 최대 1000000의 답을 받을 수 있으므로 초기화는 그보다 더 큰 +1로 설정
    curr_sum = sequence[left]
    while right < len(sequence):
        if curr_sum < k:  # right 한 칸 이동
            right += 1
            if right < len(sequence):
                curr_sum += sequence[right]
            
        elif curr_sum > k:  # left 한 칸 이동
            curr_sum -= sequence[left]
            left += 1
            
        else:  # 업데이트
            curr_length = right-left+1
            if min_length > curr_length:
                min_length = curr_length
                answer = [left, right]
            right += 1
            if right < len(sequence):
                curr_sum += sequence[right]
    
    return answer