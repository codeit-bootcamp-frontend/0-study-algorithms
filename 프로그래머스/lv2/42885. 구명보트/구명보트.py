def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    curr_min = (people[-1], len(people)-1) # 가장 적은 몸무게와 인덱스를 저장
    
    for i, weight in enumerate(people):
        rest = limit - weight
        # 현재 사람 1을 태운 보트에 나머지 사람이 가장 적은 몸무게를 태울 수 있다면
        # 사람 1보다 더 적은 몸무게의 사람도 마찬가지로 가장 적은 몸무게의 사람과 탈 수 있으므로
        # 현재 상황이 가장 꽉 차게 태울 수 있다. 
        if rest >= curr_min[0]:
            if i <= curr_min[1]:
                answer += 1
                next_min_idx = curr_min[1] - 1
                curr_min = (people[next_min_idx], next_min_idx)
            else: # 더 이상 뒤에 태울 사람이 없으므로 종료
                return answer
            
        else:
            answer += 1
                
    return answer
    