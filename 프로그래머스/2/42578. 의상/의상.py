def solution(clothes):
    answer = 1
    sorted_clothes = {}
    for name, sort in clothes:
        if sort not in sorted_clothes:
            sorted_clothes[sort] = 1
        else:
            sorted_clothes[sort] += 1
            
    for value in sorted_clothes.values():
        answer *= (value + 1)
    
    return answer - 1