def solution(weights):
    answer = 0
    weights_dict = {}
    for weight in weights:
        if weight not in weights_dict:
            weights_dict[weight] = 1
        else:
            weights_dict[weight] += 1
    
    for weight, num in weights_dict.items():
        if num > 1:
            answer += num*(num-1) // 2
        if (weight % 2 == 0) and (weight // 2 * 3) in weights_dict:
            answer += num * weights_dict[(weight // 2 * 3)]
        if weight * 2 in weights_dict:
            answer += num * weights_dict[weight * 2]
        if weight % 3 == 0 and (weight // 3 * 4) in weights_dict:
            answer += num * weights_dict[(weight // 3 * 4)]
    return answer