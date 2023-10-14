def solution(triangle):
    sum_list = [triangle[0]]
    
    for line in triangle[1:]:
        # 다음 줄의 첫 원소
        sum_list.append([sum_list[-1][0] + line[0]])
        # 다음 줄의 중간 원소들
        for i, num_in_middle in enumerate(line[1:-1]):
            bigger_num = num_in_middle + max(sum_list[-2][i], sum_list[-2][i+1])
            sum_list[-1].append(bigger_num)
        # 다음 줄의 마지막 원소
        sum_list[-1].append(sum_list[-2][-1] + line[-1])

    return max(sum_list[-1])