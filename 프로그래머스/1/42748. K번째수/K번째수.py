def solution(array, commands):
    answer = []
    for command in commands:
        left = command[0]
        right = command[1]
        sort_list = sorted(array[left-1:right])
        answer.append(sort_list[command[2] - 1])
    
    return answer