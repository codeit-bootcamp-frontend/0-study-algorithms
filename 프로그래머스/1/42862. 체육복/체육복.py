def solution(n, lost, reserve):
    answer = 0
    not_listen_num = 0
    
    
    lost_set = set(sorted(lost))
    reserve_set = set(sorted(reserve))
    common_set = lost_set & reserve_set
    lost_set -= common_set
    reserve_set -= common_set
    
    for lost_person in lost_set:
        if lost_person - 1 in reserve_set:
            reserve_set.remove(lost_person - 1)
        elif lost_person + 1 in reserve_set:
            reserve_set.remove(lost_person + 1)
        else:
            not_listen_num += 1
                
    return n - not_listen_num