def solution(s):
    answer = 0
    
    # stack 
    for _ in range(len(s)):
        isCorrect = True
        stack = []
        for i in range(len(s)):
            # 여는 괄호
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            # 닫는 괄호
            else:
                if s[i] == ')':
                    if stack and stack[-1] == '(':
                        stack.pop()
                    else:
                        isCorrect = False
                        break
                elif s[i] == ']':
                    if stack and stack[-1] == '[':
                        stack.pop()
                    else:
                        isCorrect = False
                        break
                else:
                    if stack and stack[-1] == '{':
                        stack.pop()
                    else:
                        isCorrect = False
                        break
        if not stack and isCorrect:
            answer += 1
        s = s[1:] + s[0]
            
        
    return answer