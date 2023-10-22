def solution(n, works):
    answer = 0
    if sum(works) <= n:
        return answer
    
    works.sort(reverse = True)
    idx = 0
    # 모든 값을 같게 만들어
    while idx < len(works) - 1 and n > 0:
        compare = works[idx] - works[idx + 1]
        if compare > 0:
            while works[idx] > works[idx+1] and n > 0:
                for i in range(idx+1):
                    if n == 0:
                        break
                    works[i] -= 1
                    n -= 1
        idx += 1
       
    # 나머지 있으면 분배
    while n > 0:
        for i in range(len(works)):
            if n == 0:
                break
            works[i] -= 1
            n -= 1
    
    for num in works:
        answer += num * num
    return answer