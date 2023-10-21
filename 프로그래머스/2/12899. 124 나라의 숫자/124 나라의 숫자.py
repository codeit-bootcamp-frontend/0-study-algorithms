def solution(n):
    answer = ''
    while n > 3:
        quotient = n // 3
        remainder = n % 3
        if remainder == 0:
            quotient -= 1
            remainder = 3
        answer = "124"[remainder - 1] + answer
        n = quotient
    remainder = n % 3
    if remainder == 0:
        remainder = 3
    return "124"[remainder - 1] + answer