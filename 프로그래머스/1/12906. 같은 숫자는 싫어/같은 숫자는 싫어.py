def solution(arr):
    ans = [arr[0]]
    for element in arr[1:]:
        if element != ans[-1]:
            ans.append(element)
        
    return ans