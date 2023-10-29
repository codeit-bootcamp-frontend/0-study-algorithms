def solution(s):
    answer = 0
    length = len(s)
    for i, sub in enumerate(s):
        # 전과 후가 같을 때
        consecutive = 1
        next_i = i + 1
        prev_i = i - 1
        while prev_i >= 0 and next_i < length:
            if s[prev_i] == s[next_i]:
                consecutive += 2
                next_i += 1
                prev_i -= 1
            else:
                break
        answer = max(answer, consecutive)
        
        # 전과 같을 때
        consecutive = 1
        next_i = i
        prev_i = i - 1
        while prev_i >= 0 and next_i < length:
            if s[prev_i] == s[next_i]:
                consecutive += 2
                next_i += 1
                prev_i -= 1
            else:
                break
        answer = max(answer, consecutive - 1)
    return answer