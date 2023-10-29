from math import gcd

def check_common_div(array, GCD):
    for i in range(len(array)-1, -1, -1):
        if array[i] % GCD == 0:
            return False
    return True

def solution(arrayA, arrayB):
    answer = 0
    
    GCD_A = arrayA[0]
    for i in range(1, len(arrayA)):
        GCD_A = gcd(GCD_A, arrayA[i])
    GCD_B = arrayB[0]
    for i in range(1, len(arrayB)):
        GCD_B = gcd(GCD_B, arrayB[i])
    
    check_GCD_A, check_GCD_B = check_common_div(arrayB, GCD_A), check_common_div(arrayA, GCD_B)
    
    if not check_GCD_A and not check_GCD_B:
        return 0
    elif not check_GCD_A:
        return GCD_B
    elif not check_GCD_B:
        return GCD_A
    return max(GCD_A, GCD_B)