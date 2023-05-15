def solution(arr1, arr2):
    answer = []
    
    for l in range(len(arr1)):
        col = []
        for r in range(len(arr2[0])): 
            curr = arr1[l][0] * arr2[0][r]
            for c in range(1, len(arr1[0])):
                curr += (arr1[l][c] * arr2[c][r])
            col.append(curr)
        answer.append(col)
            
    return answer