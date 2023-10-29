def solution(order):
    stack_list = []
    idx = 0
    for i in range(len(order)):
        stack_list.append(i + 1)
        while stack_list:
            if stack_list[-1] == order[idx]:
                idx += 1
                stack_list.pop()
            else:
                break
    return idx