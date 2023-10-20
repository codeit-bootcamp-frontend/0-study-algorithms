# s1을 s2로 조작할 때 필요한 횟수
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
    
    # a가 들어있는 위치를 리스트로 도출
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
    
    # 아래 3 경우의 이동 횟수 중 최소를 계산
    # 1. a 상관 없이 한 방향으로 계속 이동
    # 2. 특정 a 덩어리를 통과하지 않을 때
    # 2-1. a 덩어리 왼쪽 이동 후 오른쪽으로 돌아가기
    # 2-2. a 덩어리 오른 쪽 이동 후 왼쪽으로 돌아가기
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

    # 각 문자를 A에서 조작할 때 필요한 횟수의 합 계산
    for s in name:
        change_str_num += cal_num_mani_str("A", s)
    # 조작할 문자로 이동하는 횟수 + 각 문자 조작 횟수
    return move_pos_num + change_str_num