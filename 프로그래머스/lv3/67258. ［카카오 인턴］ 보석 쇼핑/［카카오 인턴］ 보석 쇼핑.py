def solution(gems):
    left, right = 0, 0
    min_range = 100000
    
    curr_gem_list = {gems[0]: 1}
    curr_gems = set([gems[0]])
    total_gems = len(set(gems))
    
    # 투 포인터
    while right < len(gems):
        if len(curr_gems) < total_gems:
            right += 1
            if right == len(gems):
                break
            if gems[right] not in curr_gem_list:
                curr_gem_list[gems[right]] = 1
            else:
                curr_gem_list[gems[right]] += 1
            curr_gems.add(gems[right])
            
        elif len(curr_gems) == total_gems:
            if min_range > (right - left + 1):
                min_range = right - left + 1
                result = [left+1, right+1]
                
            curr_gem_list[gems[left]] -= 1
            if curr_gem_list[gems[left]] == 0:
                curr_gems.remove(gems[left])
                
            left += 1
            
    return result
                
    