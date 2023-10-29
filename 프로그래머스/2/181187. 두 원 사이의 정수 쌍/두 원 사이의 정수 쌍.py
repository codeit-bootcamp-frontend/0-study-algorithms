def solution(r1, r2):
    answer = 0
    r1_d = r1*r1
    r2_d = r2*r2
    # 축 위 갯수
    answer += (r2 - r1 + 1) * 4

    # 사분면 위 갯수
    x = 1
    y1 = r1
    y2 = r2 - 1
    res = 0
    for x in range(1, r2):
        x_square = x*x
        while (x_square + y2*y2) > r2_d:
            y2 -= 1
        while y1-1 > 0 and (x_square + (y1-1)*(y1-1)) >= r1_d:
            y1 -= 1
        if y2 < y1:
            break
        res += (y2 - y1) + 1
            
    answer += res * 4
    
    return answer