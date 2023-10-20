def cal_num_mani_str(s1, s2):
    s1_ord = ord(s1)
    s2_ord = ord(s2)
    return min(s2_ord - s1_ord, s1_ord + 26 - s2_ord)
    

def solution(name):
    answer = 0
    a_list = []
    length = len(name)
    move_pos_num = length - 1
    change_str_num = 0
    
    is_before_a = False
    for i, s in enumerate(name):
        if i == 0:
            continue
        if s == "A":
            if not is_before_a:
                is_before_a = True
                a_list.append([i])
            else:
                continue
        else:
            if not is_before_a:
                continue
            else:
                a_list[-1].append(i-1)
            is_before_a = False
            
    if a_list and len(a_list[-1]) == 1:
        a_list[-1].append(-1)
    print(a_list)
    for s, e in a_list:
        if s == 1 and e == -1:
            move_pos_num = 0
            break
        elif s == 1:
            move_pos_num = min(move_pos_num, length - e - 1)
        elif e == -1:
            move_pos_num = min(move_pos_num, s - 1)
        else:
            left_dir = (s - 1) + (length - (e - s) - 2)
            right_dir = (length - e - 1) + (length - (e - s) - 2)
            move_pos_num = min(move_pos_num, min(left_dir, right_dir))

    for s in name:
        change_str_num += cal_num_mani_str("A", s)
    
    return move_pos_num + change_str_num