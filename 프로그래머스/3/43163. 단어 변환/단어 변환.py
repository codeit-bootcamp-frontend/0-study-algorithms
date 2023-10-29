from collections import deque
import copy

def solution(begin, target, words):
    length = len(words)
    word_length = len(begin)
    # words에 target 없으면 볼 것도 없이 0 return
    if target not in words:
        return 0
    
    queue = deque()
    queue.append((begin, 0, [False for _ in range(length)]))
    
    while queue:
        word, move_num, curr_visited = queue.popleft()
        # target인지 확인
        if word == target:
            return move_num
        
        # 다음 단어 이동하기
        for next_idx in range(length):
            # 아직 변환되지 않은 단어이고
            if curr_visited[next_idx] == False:
                # 다음 단어로 가능할 때
                diff_str_num = 0
                for i in range(word_length):
                    if word[i] != words[next_idx][i]:
                        diff_str_num += 1
                if diff_str_num == 1:
                    next_visited = copy.deepcopy(curr_visited)
                    next_visited[next_idx] = True
                    queue.append((words[next_idx], move_num + 1, next_visited))
    
    return 0