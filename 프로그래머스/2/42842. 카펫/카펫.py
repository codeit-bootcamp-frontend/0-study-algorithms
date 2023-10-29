import math

def solution(brown, yellow):
    answer = []
    for i in range(1, math.floor(math.sqrt(yellow)) + 1):
        if yellow % i == 0:
            garo = (yellow // i) + 2
            sero = i + 2
            if brown == (garo * sero) - ((garo - 2) * (sero - 2)):
                return [garo, sero]
    return answer