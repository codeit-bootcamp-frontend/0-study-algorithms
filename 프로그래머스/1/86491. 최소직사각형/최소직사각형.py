def solution(sizes):
    curr_garo = 0
    curr_sero = 0
    wallet_size = 1000000
    for size in sizes:
        next_garo_without_rotate = max(curr_garo, size[0])
        next_sero_without_rotate = max(curr_sero, size[1])
        size_without_rotate = next_garo_without_rotate * next_sero_without_rotate
        
        next_garo_with_rotate = max(curr_garo, size[1])
        next_sero_with_rotate = max(curr_sero, size[0])
        size_with_rotate = next_garo_with_rotate * next_sero_with_rotate
        
        if size_without_rotate < size_with_rotate:
            curr_garo = next_garo_without_rotate
            curr_sero = next_sero_without_rotate
            wallet_size = size_without_rotate
        else:
            curr_garo = next_garo_with_rotate
            curr_sero = next_sero_with_rotate
            wallet_size = size_with_rotate
            
    return wallet_size