def isAllSame(arr, startX, startY, length):
    num = arr[startX][startY]
    for x in range(startX, startX+length):
        for y in range(startY, startY+length):
            if num != arr[x][y]:
                return False
    return True


def recursion(arr, x, y, length, answer):
    if isAllSame(arr, x, y, length):
        answer[arr[x][y]] += 1
        return
    
    if length == 2:
        answer[arr[x][y]] += 1
        answer[arr[x+1][y]] += 1
        answer[arr[x][y+1]] += 1
        answer[arr[x+1][y+1]] += 1
        return
    
    next_length = int(length/2)
    
    recursion(arr, x, y, next_length, answer)
    recursion(arr, x+next_length, y, next_length, answer)
    recursion(arr, x, y+next_length, next_length, answer)
    recursion(arr, x+next_length, y+next_length, next_length, answer)

def solution(arr):
    answer = [0, 0]
    
    recursion(arr, 0, 0, len(arr), answer)
    
    return answer