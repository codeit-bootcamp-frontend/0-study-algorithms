def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []
    for curr_day, curr_price in enumerate(prices):
        while stack:
            if curr_price < stack[-1][1]:
                day, price = stack.pop()
                answer[day] = curr_day - day
            else:
                break
        stack.append((curr_day, curr_price))
        
    # 마지막 날까지 도달 후 남은 가격 처리
    end_day = len(prices) - 1
    while stack:
        day, price = stack.pop()
        answer[day] = end_day - day
        
    return answer