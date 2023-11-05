def solution(num):
    iter_num = 0
    while iter_num < 500:
        if num == 1:
            return iter_num
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        iter_num += 1
    return -1