from itertools import permutations
import math

def check_primary(num):
    if num < 3:
        if num == 2:
            return True
        return False
    if num % 2 == 0:
        return False
    for i in range(3, math.floor(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    num_set = set
    digit_list = []
    for number in numbers:
        digit_list.append(number)
    check_set = set()
    for using_digit_num in range(1, len(digit_list) + 1):
        for group in permutations(digit_list, using_digit_num):
            new_num = ""
            for digit in group:
                new_num += digit
            check_set.add(int(new_num))
    
    for check_num in check_set:
        if check_primary(check_num):
            answer += 1
    return answer