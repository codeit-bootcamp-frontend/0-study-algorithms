def move(n, s, p, d, answer):
    if n < 1:
        return
    
    # 1. (n-1)개의 원판을 경유지에 옮긴다.
    move(n-1, s, d, p, answer)
    # 2. 마지막에 있는 원판을 도착지에 옮긴다.
    # print(f"{n}: {s} -> {d} 이동")
    answer.append([s, d])
    # 3. (n-1)개의 원판을 도착지에 옮긴다.
    move(n-1, p, s, d, answer)
    

def solution(n):
    answer = []
    move(n, 1, 2, 3, answer)
    return answer
    