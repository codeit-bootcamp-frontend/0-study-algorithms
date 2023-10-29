import sys
N, new_score, P = map(int, sys.stdin.readline().strip().split())

if N == 0:
    print(1)
else:
    rank = 1
    consider_same_score_rank = 1
    is_include = True
    score_arr = list(map(int, sys.stdin.readline().strip().split()))
    for compare in score_arr:
        # 점수가 낮을 때
        if compare > new_score:
            rank += 1
            consider_same_score_rank += 1
        # 점수가 같을 때
        if compare == new_score:
            consider_same_score_rank += 1
        if consider_same_score_rank > P:
            is_include = False
            break

    if not is_include:
        print(-1)
    else:
        print(rank)