def solution(N, number):
    if N == number:
        return 1
    value_list = []
    answer = 1
    
    while (answer <= 8):
        # answer번 나란히 붙인 수
        num_side_by_side = 0
        for exponential in range(answer):
            num_side_by_side += 10 ** exponential * N
        value_list.append(set())
        value_list[-1].add(num_side_by_side)

        # (1, answer - 1), (2, answer - 2), ... 의 사칙연산으로 도출되는 수
        for left_index in range(answer-1):
            right_index = answer - left_index - 2
            for left_num in list(value_list[left_index]):
                for right_num in list(value_list[right_index]):
                    value_list[-1].add(left_num + right_num)
                    value_list[-1].add(left_num - right_num)
                    value_list[-1].add(left_num * right_num)
                    if right_num != 0:
                        value_list[-1].add(left_num // right_num)
        if (number in value_list[-1]):
            return answer
        
        answer += 1
        
    return -1 # -1