def solution(ingredient):
    answer = 0
    stack = []
    
    for ingr in ingredient:
        stack.append(ingr)
        if stack[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                stack.pop()
                
    return answer