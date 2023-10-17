def solution(citations):
    answer = 0
    citations.sort()
    pointer = 0

    for n in range(0, len(citations) + 1):
        # 비교 수가 더 크면 포인터 이동
        while (pointer < len(citations) and n > citations[pointer]):
            pointer += 1
            
        upper_num = len(citations) - pointer
        if upper_num == n:
            return n
        if upper_num < n:
            return n-1
        
    return answer
