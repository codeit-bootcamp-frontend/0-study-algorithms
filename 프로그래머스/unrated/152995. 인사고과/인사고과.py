def solution(scores):
    wonho = scores[0]
    
    scores.sort(key=lambda x: (-x[0], x[1]))
    
    curr = scores[0]
    possible_list = []
    for score in scores:
        curr = [max(curr[0], score[0]), max(curr[1], score[1])]
        if score[0] < curr[0] and score[1] < curr[1]:
            if score == wonho:
                return -1
            continue
        possible_list.append(score)
            
    temp = sorted(possible_list, key=lambda x : sum(x))
    sorted_list = temp[::-1]

    if wonho == sorted_list[0]:
        return 1
    
    rank = [1]
    for i in range(1, len(sorted_list)):
        if sum(sorted_list[i]) == sum(sorted_list[i-1]):
            rank.append(rank[-1])
        else:
            rank.append(i+1)
            
        if sorted_list[i] == wonho:
            return rank[-1]
        
    
        