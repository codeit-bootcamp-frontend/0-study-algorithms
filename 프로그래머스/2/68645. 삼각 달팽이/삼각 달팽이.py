def solution(n):
    total_num = n * (n + 1) // 2
    answer = [0 for _ in range(total_num)]
    answer[0] = 1
    direction = 0
    num = 2
    row = 1
    position = 0
    move_num_per_direction = n - 1
    start = True
    while move_num_per_direction > 0:
        if direction == 0:
            for i in range(move_num_per_direction):
                position += row
                row += 1
                answer[position] = num
                num += 1
            direction += 1
        elif direction == 1:
            for i in range(move_num_per_direction):
                position += 1
                answer[position] = num
                num += 1
            direction += 1
        else:
            for i in range(move_num_per_direction):
                position -= row
                row -= 1
                answer[position] = num
                num += 1
            direction = 0
        if not start:
            move_num_per_direction -= 1    
        start = False
        
    return answer