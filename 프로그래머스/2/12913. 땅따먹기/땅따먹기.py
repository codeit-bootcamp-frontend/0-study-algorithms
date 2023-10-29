def solution(land):
    answer = 0
    score_list = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]
    score_list[0] = land[0]
    
    for row in range(1, len(land)):
        score_list[row][0] = max(score_list[row - 1][1:]) + land[row][0]
        score_list[row][1] = max(score_list[row - 1][0], score_list[row - 1][2], score_list[row - 1][3])+ land[row][1]
        score_list[row][2] = max(score_list[row - 1][0], score_list[row - 1][1], score_list[row - 1][3])+ land[row][2]
        score_list[row][3] = max(score_list[row - 1][:-1])+ land[row][3]
    return max(score_list[-1])