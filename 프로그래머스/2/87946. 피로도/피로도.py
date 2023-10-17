from itertools import permutations

def solution(k, dungeons):
    answer = 0
    len_dungeons = len(dungeons)
    
    for group in permutations(range(len_dungeons)):
        curr_tired = k
        for step, dungeon_idx in enumerate(group):
            if curr_tired < dungeons[dungeon_idx][0]:
                break
            else:
                curr_tired -= dungeons[dungeon_idx][1]
                answer = max(answer, step + 1)
                
    return answer