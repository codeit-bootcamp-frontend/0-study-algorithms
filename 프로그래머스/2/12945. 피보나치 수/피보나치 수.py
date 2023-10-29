def solution(n):
    fibbo = [0, 1, 1]
    if n < 2:
        return fibbo[n]
    for i in range(3, n + 1):
        fibbo[0] = fibbo[1]
        fibbo[1] = fibbo[2]
        fibbo[2] = (fibbo[0] + fibbo[1]) % 1234567

    return fibbo[2]