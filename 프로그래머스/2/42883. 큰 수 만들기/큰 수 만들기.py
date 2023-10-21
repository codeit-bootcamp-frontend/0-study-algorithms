def solution(number, k):
    length = len(number)
    compare_stack = []
    num_excluded = 0
    i = 0
    while num_excluded < k and i < length:
        curr_num = number[i]
        # 다음 숫자와 stack을 비교해서 작은 숫자는 스택에서 제거
        while compare_stack and num_excluded < k:
            if compare_stack[-1] < curr_num:
                compare_stack.pop()
                num_excluded += 1
            else:
                break
        compare_stack.append(curr_num)
        i += 1
    
    answer = ""
    if len(compare_stack) == length:
        for n in compare_stack[:-1]:
            answer += n
    else:
        for n in compare_stack:
            answer += n
    answer += number[i:]

    return answer