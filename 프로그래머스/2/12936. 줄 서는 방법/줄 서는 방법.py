    

def solution(n, k):
    if n == 1:
        return [1]
    factorial = [-1 for _ in range(n)]
    factorial[0], factorial[1] = 1, 1
    def cal_factorial(num):
        if num <= 1:
            return 1
        if factorial[num] != -1:
            return factorial[num]
        factorial[num] = num * cal_factorial(num-1)
        return factorial[num]
        
    answer = []
    cal_factorial(n-1)
    num_list = [i+1 for i in range(n)]
    while n > 1:
        quotient = (k - 1) // factorial[n-1]
        answer.append(num_list.pop(quotient))
        k = (k - 1) % factorial[n-1] + 1
        n -= 1
    answer.append(num_list[0])
    return answer