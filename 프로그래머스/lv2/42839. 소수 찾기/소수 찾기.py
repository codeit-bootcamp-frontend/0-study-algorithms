from itertools import *


def isPrimeNumber(n):
    if n == 0 or n == 1:
        return False 
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = set()
    
    num_list = [i for i in numbers]
    cases = []
    
    for i in range(1, len(num_list)+1):
        cases += list(permutations(num_list, i))

    # print(cases)
    for case in cases:
        num = int(''.join(case))
        if isPrimeNumber(num):
            answer.add(num)
        
    result = list(answer)
    return len(result)