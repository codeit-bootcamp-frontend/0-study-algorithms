def solution(storey):
    answer = 0
    length = str(storey)
    while storey != 0:
        last_num_str = str(storey)[-1]
        last_num = int(last_num_str)
        if last_num > 5:
            answer += 10 - last_num
            storey += 10 - last_num
        elif last_num < 5 and last_num > 0:
            answer += last_num
            storey -= last_num
        elif last_num == 5:
            answer += last_num
            if storey < 10:
                storey -= last_num
            else:
                last_second_num_str = str(storey)[-2]
                last_second_num = int(last_second_num_str)
                if last_second_num >= 5:
                    storey += last_num
                else:
                    storey -= last_num
                
        storey //= 10
    return answer