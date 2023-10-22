def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    A_idx = 0
    B_idx = 0
    B_end_idx = len(B)
    
    while A_idx < len(A) and B_idx < B_end_idx:
        if A[A_idx] < B[B_idx]:
            answer += 1
            A_idx += 1
            B_idx += 1
        else:
            A_idx += 1
            B_end_idx -= 1
    
    return answer