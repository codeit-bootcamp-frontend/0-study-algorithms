def solution(dirs):
    answer = 0
    road_R_list = [[False for _ in range(-10, 10)] for _ in range(-10, 10)]
    road_U_list = [[False for _ in range(-10, 10)] for _ in range(-10, 10)]
    
    def check_move_is_first_and_register(x, y, move_s):
        if move_s == "L":
            x -= 1
            move_s = "R"
        elif move_s == "D":
            y -= 1
            move_s = "U"
        if move_s == "R":
            if not road_R_list[x][y]:
                road_R_list[x][y] = True
                return True
            else:
                return False
        else:
            if not road_U_list[x][y]:
                road_U_list[x][y] = True
                return True
            else:
                return False            
                
    
    def check_validate_move(next_x, next_y):
        if next_x < -5 or next_x > 5 or next_y < -5 or next_y > 5:
            return False
        return True
    
    def cal_move_change(s):
        if s == "U":
            return (0, 1) # x, y
        if s == "D":
            return (0, -1)
        if s == "L":
            return (-1, 0)
        else:
            return (1, 0)
    
    x, y = 0, 0
    for dir in dirs:
        move_x, move_y = cal_move_change(dir)
        next_x, next_y = x + move_x, y + move_y
        if not check_validate_move(next_x, next_y):
            continue
        if check_move_is_first_and_register(x, y, dir):
            answer += 1
        x, y = next_x, next_y
    return answer