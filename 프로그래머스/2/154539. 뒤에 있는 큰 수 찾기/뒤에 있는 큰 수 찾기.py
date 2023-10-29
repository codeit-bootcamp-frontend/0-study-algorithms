def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    stack_list = []
    for i, num in enumerate(numbers):
        while stack_list:
            if stack_list[-1][1] < num:
                last_idx, last_num = stack_list.pop()
                answer[last_idx] = num
            else:
                break
        stack_list.append((i, num))
        
    return answer