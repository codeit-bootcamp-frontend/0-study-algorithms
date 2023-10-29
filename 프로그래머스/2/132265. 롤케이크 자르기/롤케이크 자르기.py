def cal_unique_num(dict):
    # values에서 0 이상인 값을 비교하는 것이 아닌 keys의 갯수를 비교하는 것이 핵심
    return len(dict.keys())

def solution(topping):
    answer = 0
    
    length = len(topping)
    if length == 1:
        return 0
    
    left = {}
    left[topping[0]] = 1
    right = {}
    for i in range(1, length):
        if topping[i] not in right:
            right[topping[i]] = 1
        else:
            right[topping[i]] += 1
            
    if cal_unique_num(left) == cal_unique_num(right):
        answer += 1
    
    for pointer in range(1, length):
        # 왼 쪽에 추가
        if topping[pointer] not in left:
            left[topping[pointer]] = 1
        else:
            left[topping[pointer]] += 1
        # 오른 쪽에서 제거
        if right[topping[pointer]] > 0:
            right[topping[pointer]] -= 1
        if right[topping[pointer]] == 0:
            # 토핑 갯수가 0이 되면 keys에서 삭제해서 가짓수를 줄인다
            del right[topping[pointer]]
        # 비교
        if cal_unique_num(left) == cal_unique_num(right):
            answer += 1
            
    return answer