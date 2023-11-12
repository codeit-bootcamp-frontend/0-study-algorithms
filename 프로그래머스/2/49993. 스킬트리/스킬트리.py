from collections import deque

def solution(skill, skill_trees):
    answer = 0
    
    skill_dict = {}
    for s in skill:
        skill_dict[s] = True
    
    for skill_tree in skill_trees:
        # 순서가 있는 스킬 큐에 저장
        q = deque()
        for s in skill_tree:
            if s in skill_dict:
                q.append(s)
        # 순서에 맞게 배웠는지 확인
        idx = 0
        is_validate = True
        while q:
            cur_skill = q.popleft()
            if not skill[idx] == cur_skill:
                is_validate = False
                break
            idx += 1
        if is_validate:
            answer += 1
    
    return answer