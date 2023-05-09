def solution(A, B):
    A.sort()
    B.sort()
    
    score = 0
    
    check_idx = 0
    A_idx = 0
    while check_idx < len(B):
        if A[A_idx] < B[check_idx]:
            A_idx += 1
            score += 1
            
        check_idx += 1

    return score