def solution(numbers):
    answer = []
    
    # 2진수로 바꿨을 때..
    # 1. 첫째 자리가 '0' 또는 '01'이면 +1 한 값이 정답
    # 2. 그 외의 경우) 처음 만나는 0을 1로 바꾸고 그 전의 1을 0으로 바꾸기
    for num in numbers:
        binary = '0' + bin(num)[2:]
        # 1)
        if binary[-1] == '0' or binary[-2:] == '01':
            answer.append(num+1)
        # 2)
        else: 
            # find 0
            reverse = binary[::-1]
            for i, b in enumerate(reverse):
                if b == '0':
                    translate = reverse[:i-1] + '01' + reverse[i+1:]
                    answer.append(int('0b' + translate[::-1], 2))
                    break            
            
    return answer