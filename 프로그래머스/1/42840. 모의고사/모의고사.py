def solution(answers):
    first = [1,2,3,4,5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    first_len = len(first)
    second_len = len(second)
    third_len = len(third)
    right_num = [0, 0, 0]
    
    for i, ans in enumerate(answers):
        if ans == first[(i % first_len)]:
            right_num[0] += 1
        if ans == second[(i % second_len)]:
            right_num[1] += 1
        if ans == third[(i % third_len)]:
            right_num[2] += 1
    
    answer = [0]
    for i in range(1, 3):
        if right_num[answer[-1]] <= right_num[i]:
            if right_num[answer[-1]] == right_num[i]:
                answer.append(i)
            else:
                answer = [i]
    for i in range(len(answer)):
        answer[i] += 1
                
    return answer